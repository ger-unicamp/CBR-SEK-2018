#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep
from Interseccao_2 import Interseccao2
import plaza
 
 
 
#variaveis globais e flags------------------------------------------------------
colors=('none','black','blue','green','yellow','red','white','brown')
has_boneco = False #variavel de verificacao para pegar ou nao bonecos
labyrinth = False #para saber quando ja conhecemos o laribirinto (1a vez apenas)
#path = list() #lista com as direcoes a serem seguidas pelo trajeto (path)
number_of_inter = 6 # na FINAL trocar por 6
times = 1 #quantidade de interseccoes passadas, times pertence ao intervalo [0,number_of_inter]
way = 1 #1 se for ida (direto) ao setido do plaza, 0 se for volta (contrario) ao sentido do plaza
inter = Interseccao2() #interseccao
plaza_sentido = False #flag para o plaza (esta ou nao esta no plaza)
direcao = -1 #manipular direcao na funcao interseccao
lab_ultimo_boneco = False 
gyro_const = 4
directions_list = [-1,-1,-1]#lista ds direcoes
ultra_distance =  28
cor_inter = ('blue', 'green', 'red')
cor_invalid = ('none', 'brown', 'black')
 
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
    return min(aux)
 
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
    motorDireita.run_timed(time_sp=450, speed_sp=170)
    motorEsquerda.run_timed(time_sp=450, speed_sp=170)
    girarRobo(90)
    motorDireita.run_forever(speed_sp=170)
    motorEsquerda.run_forever(speed_sp=170)
    sleep(ultra_return/13)
    motorDireita.stop(stop_action = 'hold')
    motorEsquerda.stop(stop_action = 'hold')
    motorGarra.run_to_rel_pos(position_sp=-290, speed_sp=100, stop_action="hold")
    sleep(2)
    motorDireita.run_forever(speed_sp=-170)
    motorEsquerda.run_forever(speed_sp=-170)
    sleep(ultra_return/15)
    if way == 1:
        girarRobo(-90)
    elif way == 0:
        girarRobo(90)
        troca()
    has_boneco = True
 
def andarReto():
    motorDireita.run_forever(speed_sp=200)
    motorEsquerda.run_forever(speed_sp=200)
 
def volta():
    print('VOLTA')
    motorDireita.run_timed(time_sp=1000, speed_sp=-200)
    motorEsquerda.run_timed(time_sp=1000, speed_sp=-200)
    girarRobo(90)
    girarRobo(90)
    andarReto()
 
def alinha(sentido):
    print('ALINHA')
    motorEsquerda.stop(stop_action = 'hold')
    motorDireita.stop(stop_action = 'hold')
    while(colors[SensorCorDir.value()] != 'white') or (colors[SensorCorEsq.value()] != 'white'):
        if(colors[SensorCorDir.value()] != 'white'): #Enquanto os dois não estiverem fora da interssecção ou fora do fim de pista, alinha os dois sensores
            motorDireita.run_forever(speed_sp=-180*sentido) #em branco
        else:
            motorDireita.stop(stop_action = 'hold')
        if(colors[SensorCorEsq.value()] != 'white'):
            motorEsquerda.run_forever(speed_sp=-180*sentido)
        else:
            motorEsquerda.stop(stop_action = 'hold')
    motorEsquerda.stop(stop_action = 'hold')
    motorDireita.stop(stop_action = 'hold')
 
def interseccao(old_color, cor):#NOTE: tratar o caso da ultima interseccao (times==3)
    print('ESTOU NA INTERSECCAO ')
    print('old_color: ' + str(old_color) + 'color: ' + str(cor))
    global times
    global direcao
    global lab_ultimo_boneco # flag para nao veh o boneco antes da ultima interseccao
    global labyrinth
    global has_boneco
    motorDireita.run_forever(speed_sp=150)
    motorEsquerda.run_forever(speed_sp=150)
    sleep(1.8)

    if(lab_ultimo_boneco == True):
        lab_ultimo_boneco = False 
    if labyrinth:
        if way == 1: times+=1 #sentido direto, acrescenta interseccao
        else: times -= 1#sentido contrario, diminui interseccao
        if times==1:
            andarReto()
            sleep(0.02)
            troca()
            volta()
            andarReto()
        #    times = 1
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
        if (colors[old_color] in cor_inter):
            if inter.acessa(old_color)==-1:
                inter.push(old_color)                
            if (times==number_of_inter-1 and not has_boneco): # ultima interseccao
                print('ultima interseccao e push no color')
                direcao = inter.acessa(cor) 
             #   motorDireita.run_forever(speed_sp=200)
             #   motorEsquerda.run_forever(speed_sp=200)
             #   sleep(1)
                if direcao == 0:
                    girarRobo(90)
                elif direcao == 2:
                    girarRobo(-90)
                alinha(-1)
                motorDireita.run_forever(speed_sp=200)
                motorEsquerda.run_forever(speed_sp=200)
                sleep(5)
                times = number_of_inter
                troca()
                volta()
                lab_ultimo_boneco = True
                return
            
            times += 1 #atualiza as interseccoes passadas dps de ter certeza que passoudef manobra1():
        if inter.acessa(cor) != -1:
            direcao = inter.acessa(cor)
        else:
            direcao = inter.processa()
        if direcao == 0:#direita
            girarRobo(90)
            alinha(-1)
            motorDireita.run_forever(speed_sp=200)
            motorEsquerda.run_forever(speed_sp=200)
            sleep(0.1)
            andarReto()
        elif direcao == 1:#frente
            alinha(-1)
            motorDireita.run_forever(speed_sp=200)
            motorEsquerda.run_forever(speed_sp=200)
            sleep(0.1)
            andarReto()
        else:#esquerda
            girarRobo(-90)
            alinha(-1)
            motorDireita.run_forever(speed_sp=200)
            motorEsquerda.run_forever(speed_sp=200)
            sleep(0.1)
            andarReto()
    if(times == number_of_inter):
        labyrinth = True
        print('LABYRINTH9999999999999999999999999999999999999999999999')
    print('times : ' + str(times))
    sleep(1.4)
 
def manobra1():
    print("ENTREI NA MANOBRA!! ")
    motorEsquerda.stop(stop_action='hold')
    motorDireita.stop(stop_action='hold')
    cor_esquerda = SensorCorEsq.value()
    cor_direita = SensorCorDir.value()
    booleano =  colors[SensorCorDir.value()] in cor_invalid
    motorEsquerda.run_forever(speed_sp = -200)
    motorDireita.run_forever(speed_sp = -200)
    sleep(0.8)
    motorEsquerda.stop(stop_action='hold')
    motorDireita.stop(stop_action='hold')
    #motorEsquerda.run_timed(time_sp=1500, speed_sp=-200)
    #motorDireita.run_timed(time_sp=1500, speed_sp=-200)
    if booleano:
        girarRobo(-17)
        alinha(-1)
        motorEsquerda.run_forever(speed_sp = -200)
        motorDireita.run_forever(speed_sp = -200)
        sleep(0.8)
        #motorEsquerda.run_timed(time_sp=1500, speed_sp=-170)
        #motorDireita.run_timed(time_sp=1500, speed_sp=-170)
    elif not booleano:
        girarRobo(17)
        alinha(-1)
        motorEsquerda.run_forever(speed_sp = -200)
        motorDireita.run_forever(speed_sp = -200)
        sleep(0.8)
        #motorEsquerda.run_timed(time_sp=1500, speed_sp=-170)
        #motorDireita.run_timed(time_sp=1500, speed_sp=-170)
    motorEsquerda.stop(stop_action='hold')
    motorDireita.stop(stop_action='hold')

def manobra_interseccao():
    motorEsquerda.stop(stop_action='hold')
    motorDireita.stop(stop_action='hold')
    if colors[SensorCorDir.value()] in cor_invalid:
        if(inter.acessa(SensorCorEsq.value()) == 1):
            manobra1()
           # interseccao(SensorCorEsq.value(),SensorCorEsq.value())
            return 
        while colors[SensorCorDir.value()] in cor_invalid:
            motorDireita.run_forever(speed_sp=-150)
            motorEsquerda.run_forever(speed_sp=-150)
        motorEsquerda.stop(stop_action='hold')
        motorDireita.stop(stop_action='hold')
        motorEsquerda.run_timed(time_sp=800, speed_sp=-170)
        motorDireita.run_timed(time_sp=800, speed_sp=-170)
        motorEsquerda.stop(stop_action='hold')
        motorDireita.stop(stop_action='hold')
        motorEsquerda.run_timed(time_sp=1000, speed_sp=-180)
    elif colors[SensorCorEsq.value()] in cor_invalid:
        if(inter.acessa(SensorCorDir.value()) == 1):
            manobra1()
            return 
        while colors[SensorCorDir.value()] in cor_invalid:
            motorDireita.run_forever(speed_sp=-150)
            motorEsquerda.run_forever(speed_sp=-150)
        motorEsquerda.stop(stop_action='hold')
        motorDireita.stop(stop_action='hold')
        motorEsquerda.run_timed(time_sp=800, speed_sp=-170)
        motorDireita.run_timed(time_sp=800, speed_sp=-170)
        motorEsquerda.stop(stop_action='hold')
        motorDireita.stop(stop_action='hold')
        motorDireita.run_timed(time_sp=1000, speed_sp=-180)
 
def plaza_funcao():
    global plaza_sentido
    global times
    plaza_sentido = True
    '''
    motorDireita.stop(stop_action = 'hold')
    motorEsquerda.stop(stop_action = 'hold')
    while(colors[SensorCorDir.value()] == 'white' and colors[SensorCorEsq.value()] == 'white'):
        motorEsquerda.run_forever(speed_sp=50)
        motorDireita.run_forever(speed_sp=50)
    motorDireita.stop(stop_action = 'hold')
    motorEsquerda.stop(stop_action = 'hold')
    if(colors[SensorCorDir.value()] == 'red'):
        while(colors[SensorCorDir.value()] == 'red'):
            motorDireita.run_forever(speed_sp = -50)
        motorDireita.stop(stop_action = 'hold')
    if(colors[SensorCorEsq.value()] == 'red'):
        while(colors[SensorCorEsq.value()] == 'red'):
            motorEsquerda.run_forever(speed_sp = -50)
        motorEsquerda.stop(stop_action = 'hold')
    #comentra aqui alinha
    '''
  #  motorEsquerda.run_forever(speed_sp=100)
  #  motorDireita.run_forever(speed_sp=100)
  #  sleep(4) #entrar no plaza
    print('vou entrar no plaza')
    plaza.plaza()
    has_boneco = False


 
 
#funcao main -------------------------------------------------------------------
def main():
    global has_boneco
    global plaza_sentido
    global labyrinth
    global times
    global cor_inter
    global ultra_distance
    global lab_ultimo_boneco
 
    btn = Button()
    calibraGyro()
    cor = 0 #none
    Sound.speak('Hello Humans!').wait()
    motorGarra.run_to_rel_pos(position_sp=290, speed_sp=100, stop_action="hold") # abrir garra
    print(ultrassonico.value())
 
    while not btn.any():
        if colors[SensorCorDir.value()] == 'white' and colors[SensorCorEsq.value()] == 'white':
           # print("bloco:branco")
            andarReto()
            ultra_return = ultra()
   
            if ultra_return < ultra_distance and not has_boneco and not plaza_sentido and not lab_ultimo_boneco:
                captura(ultra_return)#caso way == 0, a funcao troca() eh chamada dentro da funcao agarrarBoneco()
   
        elif (colors[SensorCorDir.value()] != 'white') or (colors[SensorCorEsq.value()] != 'white'):
            print('bloco: diferente de branco')  
            print('plaza: ' + str(plaza_sentido))   
            motorDireita.run_timed(time_sp=400, speed_sp=200)
            motorEsquerda.run_timed(time_sp=400, speed_sp=200)   
            if not plaza_sentido:
                print('bloco:volta ou manobra')
                if (colors[SensorCorDir.value()] in cor_invalid) or (colors[SensorCorEsq.value()] in cor_invalid):
                    sleep(0.2)
                    if (colors[SensorCorDir.value()] in cor_invalid) and (colors[SensorCorEsq.value()] in cor_invalid): #Condição Fim de rua (Pós sleep)
                        alinha(1)
                        cor = 0 #caso de rua sem saida: old_color recebe 0 novamente
                        volta()
             
                    elif (colors[SensorCorDir.value()] in cor_invalid and colors[SensorCorEsq.value()] == 'white') or (colors[SensorCorEsq.value()] in cor_invalid and colors[SensorCorDir.value()] == 'white'):
                        manobra1()
                    elif(colors[SensorCorDir.value()] in cor_inter and colors[SensorCorEsq.value()] in cor_invalid) or (colors[SensorCorEsq.value()] in cor_inter and colors[SensorCorDir.value()] in cor_invalid):
                        print('manobra interseccao')
                        manobra_interseccao()

            if colors[SensorCorEsq.value()] in cor_inter or colors[SensorCorDir.value()] in cor_inter:
                print("qualquer cor valida")
                if(times != number_of_inter):
                    motorDireita.run_forever(speed_sp=200)
                    motorEsquerda.run_forever(speed_sp=200)
                    sleep(0.8)
                if colors[SensorCorEsq.value()]=='white' and times != number_of_inter:
                    print('sit: branco e valido')
                    motorDireita.run_forever(speed_sp=-200)
                    motorEsquerda.run_forever(speed_sp=-200)
                    sleep(0.9)
                    motorDireita.stop(stop_action = 'hold')
                    motorEsquerda.stop(stop_action = 'hold')
                    while colors[SensorCorDir.value()] != 'white':
                        print('while da sit:branco e valido - esquer')
                        motorDireita.run_forever(speed_sp=-170)
                elif colors[SensorCorDir.value()]=='white' and times != number_of_inter:
                    motorDireita.run_forever(speed_sp=-200)
                    motorEsquerda.run_forever(speed_sp=-200)
                    sleep(0.9)
                    motorDireita.stop(stop_action = 'hold')
                    motorEsquerda.stop(stop_action = 'hold')
                    while colors[SensorCorEsq.value()] != 'white':
                        print('while da sit:branco e valido - direita')
                        motorEsquerda.run_forever(speed_sp=-170)
                if colors[SensorCorEsq.value()] in cor_inter and colors[SensorCorDir.value()] in cor_inter:
                    print('cor valida')
                    old_color=cor
                    cor = SensorCorDir.value()  # NOTE: pegar de um sensor só?sim
                    print('----- TIMES {} LAB: {}  HAS: {} WAY {} ----------------------'.format(times, labyrinth, has_boneco, way))
                    if times < number_of_inter or (times == number_of_inter and way == 0):
                        alinha(1)
                        interseccao(old_color, cor)
                    elif times == number_of_inter and labyrinth and has_boneco and way == 1:
                        print('       ----------------- ENTROOOOOUUUUUUUU ----------------------')
                        if(plaza_sentido == True):
                            motorDireita.stop(stop_action = 'hold')
                            motorEsquerda.stop(stop_action = 'hold')
                            '''
                            # comentar para estrategia
                            motorEsquerda.run_forever(speed_sp = -170)
                            motorDireita.run_forever(speed_sp = -170)
                            sleep(1) #testar 
                            while(colors[SensorCorDir.value()] == 'white' and colors[SensorCorEsq.value()] == 'white'):
                                motorEsquerda.run_forever(speed_sp=50)
                                motorDireita.run_forever(speed_sp=50)
                            motorDireita.stop(stop_action = 'hold')
                            motorEsquerda.stop(stop_action = 'hold')
                            if(colors[SensorCorDir.value()] != 'white'):
                                while(colors[SensorCorDir.value()] != 'white'):
                                    motorDireita.run_forever(speed_sp = -50)
                                motorDireita.stop(stop_action = 'hold')
                            if(colors[SensorCorEsq.value()] != 'white'):
                                while(colors[SensorCorEsq.value()] != 'white'):
                                    motorEsquerda.run_forever(speed_sp = -50)
                                motorEsquerda.stop(stop_action = 'hold')
                            #comentar para estrategia
                            '''
                            alinha(1)
                            motorEsquerda.run_forever(speed_sp=200)
                            motorDireita.run_forever(speed_sp=200)
                            sleep(1.2) #testar - passar pelas tres cores
                            '''
                            motorDireita.stop(stop_action = 'hold') 
                            motorEsquerda.stop(stop_action = 'hold')
                            '''
                            plaza_sentido = False
                            times = 6
                            troca()
                        else:
                            print('indo para plaza - main')
                            motorDireita.stop(stop_action = 'hold')
                            motorEsquerda.stop(stop_action = 'hold')
                            alinha(1)
                            motorEsquerda.run_forever(speed_sp=150)
                            motorDireita.run_forever(speed_sp=150)
                            sleep(4) #passar nas tres faixas de cor
                            plaza_funcao()
           
if __name__ == '__main__':
    main()

'''
motorDireita.stop(stop_action = 'hold')
motorEsquerda.stop(stop_action = 'hold')
alinha(1)

'''