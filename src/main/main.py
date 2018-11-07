#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep
from interseccao import Interseccao
import plaza



#variaveis globais e flags------------------------------------------------------
colors=('none','black','blue','green','yellow','red','white','brown')
has_boneco = False #variavel de verificacao para pegar ou nao bonecos
labyrinth = False #para saber quando ja conhecemos o laribirinto (1a vez apenas)
#path = list() #lista com as direcoes a serem seguidas pelo trajeto (path)
number_of_inter = 6 # na FINAL trocar por 6
times = 1 #quantidade de interseccoes passadas, times pertence ao intervalo [0,number_of_inter]
way = 1 #1 se for ida (direto) ao setido do plaza, 0 se for volta (contrario) ao sentido do plaza
inter = Interseccao() #interseccao
plaza = False #flag para o plaza (esta ou nao esta no plaza)
direcao = -1 #manipular direcao na funcao interseccao
gyro_const = 4
directions_list = [-1,-1,-1]#lista ds direcoes
ultra_distance = 35

# definicao de motores----------------------------------------------------------
motorDireita = LargeMotor('outC')
motorEsquerda = LargeMotor('outB')
motorGarra = MediumMotor('outA')

# definicao de sensores---------------------------------------------------------
ultrassonico = UltrasonicSensor()
assert ultrassonico.connected, "Sensor ultrassonico nao conectado"
ultrassonico.mode = 'US-DIST-CM'

SensorCorDir = ColorSensor('in1')
assert SensorCorDir.connected, "Sensor de cor nao conectado"
SensorCorDir.mode='COL-COLOR'

SensorCorEsq = ColorSensor('in4')
assert SensorCorEsq.connected, "Sensor de cor nao conectado"
SensorCorEsq.mode='COL-COLOR'

gyro = GyroSensor()
assert gyro.connected, "Giroscopio nao conectado"

#funcoes (e estados) -------------------------------------------------------------
def calibraGyro():
    gyro.mode = 'GYRO-RATE'
    sleep(0.3)
    gyro.mode = 'GYRO-ANG'
    sleep(0.3)

def troca():
    global way
    global times
    global labyrinth

    if way ==1: way=0
    else: way=1
    if times==number_of_inter and not labyrinth: labyrinth=True

def ultra():
    aux = [ultrassonico.value()/10 for i in range(10)]
    aux.sort()
    return aux[4]

def girarRobo(anguloDesejado):
    calibraGyro()
    anguloSensor = gyro.value()
    if(anguloDesejado > 0):
        while(anguloSensor < anguloDesejado - gyro_const): # 4 eh para compensar o lag de leitura do gyro
            motorDireita.run_forever(speed_sp=-200)
            motorEsquerda.run_forever(speed_sp=200)
            anguloSensor = gyro.value()
    else:
        while(anguloSensor > anguloDesejado + gyro_const): # 4 eh para compensar o lag de leitura do gyro
            motorDireita.run_forever(speed_sp=200)
            motorEsquerda.run_forever(speed_sp=-200)
            anguloSensor = gyro.value()

    motorDireita.stop(stop_action="hold")
    motorEsquerda.stop(stop_action="hold")
    calibraGyro()

def captura(ultra_return):
    global has_boneco
    print('CAPTURA')
    motorDireita.run_timed(time_sp=800, speed_sp=200)
    motorEsquerda.run_timed(time_sp=800, speed_sp=200)
    sleep(1)
    girarRobo(90)
  #  motorGarra.run_to_rel_pos(position_sp=290, speed_sp=100, stop_action="hold")
    sleep(2)
    #TESTAR
    motorDireita.run_forever(speed_sp=170)
    motorEsquerda.run_forever(speed_sp=170)
    sleep(ultra_return/13)
    motorDireita.stop(stop_action = 'hold')
    motorEsquerda.stop(stop_action = 'hold')
    motorGarra.run_to_rel_pos(position_sp=-290, speed_sp=100, stop_action="hold")
    sleep(2)
    motorDireita.run_forever(speed_sp=-170)
    motorEsquerda.run_forever(speed_sp=-170)
    sleep(ultra_return/13)
    if way == 1:
        girarRobo(-90)
    elif way == 0:
        girarRobo(90)
        troca()
    has_boneco = True

def andarReto():
    motorDireita.run_forever(speed_sp=200)
    motorEsquerda.run_forever(speed_sp=198)

def volta():
    print('VOLTA')
    motorDireita.run_timed(time_sp=800, speed_sp=-200)
    motorEsquerda.run_timed(time_sp=800, speed_sp=-200)
    girarRobo(90)
    girarRobo(90)
    andarReto()

def alinha(sentido):
    print('ALINHA')
    motorEsquerda.run_forever(speed_sp=0)
    motorDireita.run_forever(speed_sp=0)
    while(colors[SensorCorDir.value()] != 'white') or (colors[SensorCorEsq.value()] != 'white'):
        if(colors[SensorCorDir.value()] != 'white'): #Enquanto os dois não estiverem fora da interssecção ou fora do fim de pista, alinha os dois sensores
            motorDireita.run_forever(speed_sp=-100*sentido) #em branco
        else:
            motorDireita.run_forever(speed_sp=0)
        if(colors[SensorCorEsq.value()] != 'white'):
            motorEsquerda.run_forever(speed_sp=-100*sentido)
        else:
            motorEsquerda.run_forever(speed_sp=0)
    motorEsquerda.run_forever(speed_sp=0)
    motorDireita.run_forever(speed_sp=0)

def interseccao(old_color, cor):#NOTE: tratar o caso da ultima interseccao (times==3)
    print('ESTOU NA INTERSECCAO ')
    global times
    global direcao

    #motorDireita.run_timed(time_sp=1600, speed_sp=200)
    #motorEsquerda.run_timed(time_sp=1600, speed_sp=200)
    motorDireita.run_forever(speed_sp=200)
    motorEsquerda.run_forever(speed_sp=200)
    sleep(0.85)

    if labyrinth:
        if way == 1: times+=1 #sentido direto, acrescenta interseccao
        else: times -= 1#sentido contrario, diminui interseccao
        if times==0:
            andarReto()
            sleep(0.02)
            troca()
            volta()
            andarReto()
            sleep(0.03)
            times = 1
            sleep(0.2)
        else:
            direcao = inter.acessa(cor)
            if direcao == 0 and way == 1:#direita
                girarRobo(90)
                alinha(-1)
                motorDireita.run_forever(speed_sp=200)
                motorEsquerda.run_forever(speed_sp=200)
                andarReto()
            elif direcao == 0 and way == 0:#esquerda
                girarRobo(-90)
                alinha(-1)
                motorDireita.run_forever(speed_sp=200)
                motorEsquerda.run_forever(speed_sp=200)
                andarReto()
            elif direcao == 1:#frente
                alinha(-1)
                motorDireita.run_forever(speed_sp=200)
                motorEsquerda.run_forever(speed_sp=200)
                andarReto()
            elif direcao == 2 and way == 1:#esquerda
                girarRobo(-90)
                alinha(-1)
                motorDireita.run_forever(speed_sp=200)
                motorEsquerda.run_forever(speed_sp=200)
                andarReto()
            elif direcao == 2 and way == 0:#direita
                girarRobo(90)
                alinha(-1)
                motorDireita.run_forever(speed_sp=200)
                motorEsquerda.run_forever(speed_sp=200)
                andarReto()
        sleep(2)
    else:#aqui so entramos na primeira vez no sentido do plaza e way sempre sera igual a 1
        if (colors[old_color] == 'blue' or colors[old_color] == 'green' or colors[old_color] == 'red'):
            print('push no inter' + ' ' + str(old_color))
            inter.push(old_color, direcao)
            directions_list[inter.acessa(old_color)] = -2
            print(str(directions_list) + ' directions_list')
            if (times==number_of_inter-1): # ultima interseccao
                print('ultima interseccao e push no color')
                if directions_list.count(-1) == 1:
                    print('ultima direcao no push ' + str(directions_list.index(-1))+ ' cor enviada: ' + str(cor))
                    inter.push(cor, directions_list.index(-1))
                    directions_list[directions_list.index(-1)] = -2
                motorDireita.run_forever(speed_sp=200)
                motorEsquerda.run_forever(speed_sp=200)
                sleep(1.4)
                motorDireita.stop(stop_action="hold")
                motorEsquerda.stop(stop_action="hold")
                times = number_of_inter
                troca()
                volta()
                sleep(1.6)
                times = number_of_inter - 1
                return 
            else:
                times += 1 #atualiza as interseccoes passadas dps de ter certeza que passou
        direcao = inter.where_to_go(cor)
        print('direcao escolhida: '+str(direcao))
        if direcao == 0:#direita
            girarRobo(90)
            alinha(-1)
            motorDireita.run_forever(speed_sp=200)
            motorEsquerda.run_forever(speed_sp=200)
            sleep(0.5)
            andarReto()
        elif direcao == 1:#frente
            alinha(-1)
            motorDireita.run_forever(speed_sp=200)
            motorEsquerda.run_forever(speed_sp=200)
            sleep(1)
            andarReto()
        else:#esquerda
            girarRobo(-90)
            alinha(-1) 
            motorDireita.run_forever(speed_sp=200)
            motorEsquerda.run_forever(speed_sp=200)
            sleep(0.5)
            andarReto()
    print(str(inter)+' inter')
    print('times : ' + str(times))
    sleep(1.4)

def manobra1():
    print("ENTREI NA MANOBRA!! ")
    motorDireita.run_forever(speed_sp=0) #Para o robo para executar a manobra
    motorEsquerda.run_forever(speed_sp=0) #STOP ACTION
    if(colors[SensorCorDir.value()] == 'none') or (colors[SensorCorDir.value()] == 'black') or (colors[SensorCorDir.value()] == 'brown'): #confere se o sensor direito está fora da pista
        motorDireita.run_forever(speed_sp=0) #STOP ACTION
        motorEsquerda.run_forever(speed_sp=180) #Gira roda esquerda
        sleep(1.13)
        x = colors[SensorCorEsq.value()]
        if x != 'black':
            while(colors[SensorCorEsq.value()] == x):
                #print("RODANDO PARA A DIREITA")
                motorDireita.run_forever(speed_sp=0) #STOP ACTION
                motorEsquerda.run_forever(speed_sp=180) #Gira roda esquerda
            sleep(0.1)
            motorEsquerda.run_forever(speed_sp=0) #Para o robo na beirada da pista #STOP ACTION
            sleep(1)
            motorDireita.run_timed(time_sp=1100, speed_sp=-200) #Retorna ao meio da pista
            motorEsquerda.run_timed(time_sp=1100, speed_sp=-200)
            girarRobo(-90) #Gira para voltar ao percurso
        '''
        else: #Fim de pista
            print('MANOBRA FIM DE PISTA -- SENSOR DIREITO FORA')
            motorDireita.run_forever(speed_sp=-150)
            motorEsquerda.run_forever(speed_sp=0)
            sleep(1.5)
            while(colors[SensorCorDir.value()] != 'black'):
                motorDireita.run_forever(speed_sp=-150)
                motorEsquerda.run_forever(speed_sp=0)
            while(colors[SensorCorDir.value()] != 'black') or (colors[SensorCorEsq.value()] != 'black'):
                if(colors[SensorCorDir.value()] != 'black'): #Enquanto os dois não estiverem fora da interssecção ou fora do fim de pista, alinha os dois sensores
                    motorDireita.run_forever(speed_sp=-150) #em branco
                else:
                    motorDireita.run_forever(speed_sp=0)
                if(colors[SensorCorEsq.value()] != 'black'):
                    motorEsquerda.run_forever(speed_sp=-150)
                else:
                    motorEsquerda.run_forever(speed_sp=0)
            motorEsquerda.run_forever(speed_sp=0)
            motorDireita.run_forever(speed_sp=0)
        '''
    elif(colors[SensorCorEsq.value()] == 'none') or (colors[SensorCorEsq.value()] == 'black') or (colors[SensorCorEsq.value()] == 'brown'): #Tudo igual de maneira antagonica
        motorEsquerda.run_forever(speed_sp=0) #STOP ACTION
        motorDireita.run_forever(speed_sp=180)
        sleep(1.13)
        x = colors[SensorCorDir.value()]
        if x != 'black':
            while(colors[SensorCorDir.value()] == x):
                #print("RODANDO PARA A ESQUEDA")
                motorEsquerda.run_forever(speed_sp=0) #STOP ACTION
                motorDireita.run_forever(speed_sp=180)
            sleep(0.1)
            motorDireita.run_forever(speed_sp=0) #STOP ACTION
            sleep(1)
            motorDireita.run_timed(time_sp=1100, speed_sp=-200)
            motorEsquerda.run_timed(time_sp=1100, speed_sp=-200)
            girarRobo(90)
        '''
        else: #Fim de pista
            print('MANOBRA FIM DE PISTA -- SENSOR ESQUERDO FORA')
            motorDireita.run_forever(speed_sp=0)
            motorEsquerda.run_forever(speed_sp=-150)
            sleep(1.5)
            while(colors[SensorCorEsq.value()] != 'black'):
                motorEsquerda.run_forever(speed_sp=-150)
            motorEsquerda.run_forever(speed_sp=0)
            while(colors[SensorCorDir.value()] != 'black') or (colors[SensorCorEsq.value()] != 'black'):
                if(colors[SensorCorDir.value()] != 'black'): #Enquanto os dois não estiverem fora da interssecção ou fora do fim de pista, alinha os dois sensores
                    motorDireita.run_forever(speed_sp=-150) #em branco
                else:
                    motorDireita.run_forever(speed_sp=0)
                if(colors[SensorCorEsq.value()] != 'black'):
                    motorEsquerda.run_forever(speed_sp=-150)
                else:
                    motorEsquerda.run_forever(speed_sp=0)
            motorEsquerda.run_forever(speed_sp=0)
            motorDireita.run_forever(speed_sp=0)
        '''

def plaza():
    global plaza
    global times
    
    plaza = True 
    times = 7
    alinha(1)
    motorEsquerda.run_forever(speed_sp=200)
    motorDireita.run_forever(speed_sp=200)
    sleep(2.5)
    print('vou entrar no plaza')
    plaza.plaza()




#funcao main -------------------------------------------------------------------
def main():
    global has_boneco
    global plaza
    global labyrinth
    global times
 

    btn = Button()
    calibraGyro()
    cor = 0 #none
    Sound.speak('Hello Humans!').wait()
    motorGarra.run_to_rel_pos(position_sp=290, speed_sp=100, stop_action="hold") # abrir garra
    print(ultrassonico.value())
    global ultra_distance
    while not btn.any():
        if colors[SensorCorDir.value()] == 'white' and colors[SensorCorEsq.value()] == 'white':
            andarReto()
            ultra_return = ultra()
            if ultra_return < ultra_distance and not has_boneco and labyrinth and not plaza:
                captura(ultra_return)#caso way == 0, a funcao troca() eh chamada dentro da funcao agarrarBoneco()
        elif (colors[SensorCorDir.value()] != 'white') or (colors[SensorCorEsq.value()] != 'white') and not plaza: #Condição de saída de pista
            if (colors[SensorCorDir.value()] == 'none') or (colors[SensorCorDir.value()] == 'black') or (colors[SensorCorEsq.value()] =='none') or (colors[SensorCorEsq.value()] == 'black'):
                sleep(0.2)
                if (colors[SensorCorDir.value()] == 'black') and (colors[SensorCorEsq.value()] =='black'): #Condição Fim de rua (Pós sleep)
                    alinha(1)
                    cor = 0 #caso de rua sem saida: old_color recebe 0 novamente
                    volta()
                elif (colors[SensorCorDir.value()] == 'none') or (colors[SensorCorDir.value()] == 'black') or (colors[SensorCorDir.value()] == 'brown') or (colors[SensorCorEsq.value()] =='none') or (colors[SensorCorEsq.value()] == 'black'):
                    manobra1()
            elif colors[SensorCorDir.value()] != 'white' and colors[SensorCorDir.value()] != 'black' and colors[SensorCorEsq.value()] != 'white' and colors[SensorCorEsq.value()] != 'black':
                old_color = cor #dependemos da cor anterior para saber se a direcao esta correta
                sleep(0.2)
                if colors[SensorCorDir.value()] != 'white' and colors[SensorCorDir.value()] != 'black' and colors[SensorCorEsq.value()] != 'white' and colors[SensorCorEsq.value()] != 'black':
                    alinha(1)
                    motorDireita.run_forever(speed_sp=200)
                    motorEsquerda.run_forever(speed_sp=200)
                    #motorDireita.run_timed(time_sp=1000, speed_sp=200)
                    #motorEsquerda.run_timed(time_sp=1000, speed_sp=200)
                    sleep(0.3)
                    cor = SensorCorDir.value() #NOTE: pegar de um sensor só?
                    if times < number_of_inter+1:
                        interseccao(old_color, cor)
                    elif times == number_of_inter and labyrinth and has_boneco:
                        #plaza()#TODO e NOTE: mudar flag plaza
                        if(plaza == True):
                            alinha(1)
                            sleep(0.8) # passar pelas três faixas
                            plaza = False 
                            times = 6
                        else:
                            plaza()
                    elif times == number_of_inter and not labyrinth:
                        troca()
                        volta()
if __name__ == '__main__':
    main()
