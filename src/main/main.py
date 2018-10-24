#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep
from interseccao.py import Interseccao

#variaveis globais e flags------------------------------------------------------
colors=('none','black','blue','green','yellow','red','white','brown')
has_boneco = False#variavel de verificacao para pegar ou nao bonecos
labyrinth = False#para saber quando ja conhecemos o laribirinto (1a vez apenas)
#path = list() #lista com as direcoes a serem seguidas pelo trajeto (path)
number_of_inter = 4 # na FINAL trocar por 6
times = 0 #quantidade de interseccoes passadas, times pertence ao intervalo [0,number_of_inter]
way = 1 #1 se for ida (direto) ao setido do plaza, 0 se for volta (contrario) ao sentido do plaza
inter = Interseccao()#interseccao
plaza = False#flag para o plaza (esta ou nao esta no plaza)
direcao = -1#manipular direcao na funcao interseccao

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
    sleep(1)
    gyro.mode = 'GYRO-ANG'
    sleep(1)
def troca():
    if way ==1: way=0
    else: way=1
    if times==number_of_inter and not labyrinth: labyrinth=True
def ultrassonico():
    aux = [ultrassonico.value()/10 for i in range(10)]
    aux.sort()
    if aux[4] < 20: return True
    else: return False
def girarRobo(anguloDesejado):
    calibraGyro()
    anguloSensor = gyro.value()
    if(anguloDesejado > 0):
        while(anguloSensor < anguloDesejado - 4): # 4 eh para compensar o lag de leitura do gyro
            motorDireita.run_forever(speed_sp=-50)
            motorEsquerda.run_forever(speed_sp=50)
            anguloSensor = gyro.value()
    else:
        while(anguloSensor > anguloDesejado + 4): # 4 eh para compensar o lag de leitura do gyro
            motorDireita.run_forever(speed_sp=50)
            motorEsquerda.run_forever(speed_sp=-50)
            anguloSensor = gyro.value()

    motorDireita.stop(stop_action="hold")
    motorEsquerda.stop(stop_action="hold")
    calibraGyro()
def agarrarBoneco():
    motorDireita.run_timed(time_sp=500, speed_sp=200)
    motorEsquerda.run_timed(time_sp=500, speed_sp=200)
    sleep(2)
    girarRobo(90)
    sleep(2)
    motorGarra.run_to_rel_pos(position_sp=290, speed_sp=100, stop_action="hold")
    sleep(5)
    motorDireita.run_timed(time_sp=1400, speed_sp=200)
    motorEsquerda.run_timed(time_sp=1400, speed_sp=200)
    sleep(3)
    motorGarra.run_to_rel_pos(position_sp=-290, speed_sp=100, stop_action="hold")#NOTE: TESTAR GARRAS
    #de -100 a -330 a garra n subiu
    sleep(5)
    #como subir a garra?
    motorDireita.run_timed(time_sp=1400, speed_sp=-200)
    motorEsquerda.run_timed(time_sp=1400, speed_sp=-200)
    sleep(3)
    if way == 1:
        girarRobo(-90)
    else:
        girarRobo(90)
        troca()
    has_boneco = True
    calibraGyro()
def andarReto():
    motorDireita.run_forever(speed_sp=200)
    motorEsquerda.run_forever(speed_sp=200)
def volta():
    motorDireita.run_timed(time_sp=800 speed_sp=-200)
    motorEsquerda.run_timed(time_sp=800 speed_sp=-200)
    sleep(0.9)
    girarRobo(90)
    sleep(1)
    girarRobo(90)
    andarReto()
def alinha():
	motorEsquerda.run_forever(speed_sp=0)
	motorDireita.run_forever(speed_sp=0)
	while(colors[SensorCorDir.value()] != 'white') or (colors[SensorCorEsq.value()] != 'white'):
		if(colors[SensorCorDir.value()] != 'white'): #Enquanto os dois não estiverem fora da interssecção ou fora do fim de pista, alinha os dois sensores
			motorDireita.run_forever(speed_sp=-100) #em branco
		else:
			motorDireita.run_forever(speed_sp=0)
		if(colors[SensorCorEsq.value()] != 'white'):
			motorEsquerda.run_forever(speed_sp=-100)
		else:
			motorEsquerda.run_forever(speed_sp=0)
	motorEsquerda.run_forever(speed_sp=0)
	motorDireita.run_forever(speed_sp=0)
def interseccao(old_color, cor):#NOTE: tratar o caso da ultima interseccao (times==3)
    motorDireita.run_timed(time_sp=1400, speed_sp=200)
    motorEsquerda.run_timed(time_sp=1400, speed_sp=200)
    if labyrinth:
        direcao = inter.acessa(cor)
        if direcao == 0 and way == 1:#direita
            girarRobo(90)
            motorDireita.run_timed(time_sp=3000, speed_sp=200)
            motorEsquerda.run_timed(time_sp=3000, speed_sp=200)
            andarReto()
        elif direcao == 0 and way == 0:#esquerda
            girarRobo(-90)
            motorDireita.run_timed(time_sp=3000, speed_sp=200)
            motorEsquerda.run_timed(time_sp=3000, speed_sp=200)
            andarReto()
        elif direcao == 1:#frente
            motorDireita.run_timed(time_sp=3000, speed_sp=200)
            motorEsquerda.run_timed(time_sp=3000, speed_sp=200)
            andarReto()
        elif direcao == 2 and way == 1:#esquerda
            girarRobo(-90)
            motorDireita.run_timed(time_sp=3000, speed_sp=200)
            motorEsquerda.run_timed(time_sp=3000, speed_sp=200)
            andarReto()
        elif direcao == 2 and way == 0:#direita
            girarRobo(90)
            motorDireita.run_timed(time_sp=3000, speed_sp=200)
            motorEsquerda.run_timed(time_sp=3000, speed_sp=200)
            andarReto()
        if way == 1: times+=1#sentido direto, acrescenta interseccao
        else: times -= 1#sentido contrario, diminui interseccao
    else:#aqui so entramos na primeira vez no sentido do plaza e way sempre sera igual a 1
        if direcao != -1 and (colors[old_color] == 'blue' or colors[old_color] == 'green' or colors[old_color] == 'red'):
            inter.push(old_color, direcao)
            times += 1 #atualiza as interseccoes passadas dps de ter certeza que passou
        direcao = inter.where_to_go(cor)
        if direcao == 0:#direita
            girarRobo(90)
            motorDireita.run_timed(time_sp=3000, speed_sp=200)
            motorEsquerda.run_timed(time_sp=3000, speed_sp=200)
            andarReto()
        elif direcao == 1:#frente
            motorDireita.run_timed(time_sp=3000, speed_sp=200)
            motorEsquerda.run_timed(time_sp=3000, speed_sp=200)
            andarReto()
        else:#esquerda
            girarRobo(-90)
            motorDireita.run_timed(time_sp=3000, speed_sp=200)
            motorEsquerda.run_timed(time_sp=3000, speed_sp=200)
            andarReto()
def manobra1():
	print("ENTREI NA MANOBRA!! ")
	motorDireita.run_forever(speed_sp=0) #Para o robo para executar a manobra
	motorEsquerda.run_forever(speed_sp=0) #STOP ACTION
	if (colors[SensorCorDir.value()] == 'none') or (colors[SensorCorDir.value()] == 'black') or (colors[SensorCorDir.value()] == 'brown'): #confere se o sensor direito está fora da pista
		motorDireita.run_forever(speed_sp=0) #STOP ACTION
		motorEsquerda.run_forever(speed_sp=180) #Gira roda esquerda
		sleep(0.3)
		x = colors[SensorCorEsq.value()]
		print(x)
		if x != 'black':
			while(colors[SensorCorEsq.value()] == x):
				print("RODANDO PARA A DIREITA")
				motorDireita.run_forever(speed_sp=0) #STOP ACTION
				motorEsquerda.run_forever(speed_sp=180) #Gira roda esquerda
			sleep(0.1)
			motorEsquerda.run_forever(speed_sp=0) #Para o robo na beirada da pista #STOP ACTION
			sleep(1)
			motorDireita.run_timed(time_sp=1100, speed_sp=-200) #Retorna ao meio da pista
			motorEsquerda.run_timed(time_sp=1100, speed_sp=-200)
			girarRobo(-90) #Gira para voltar ao percurso
		else: #Fim de pista
			motorDireita.run_forever(speed_sp=-180)
			motorEsquerda.run_forever(speed_sp=-180)
			sleep(0.3)
			motorDireita.run_forever(speed_sp=0) #Roda
			sleep(0.3)
			motorEsquerda.run_forever(speed_sp=0)
			sleep(0.1)
	elif (colors[SensorCorEsq.value()] == 'none') or (colors[SensorCorEsq.value()] == 'black') or (colors[SensorCorEsq.value()] == 'brown'): #Tudo igual de maneira antagonica
		motorEsquerda.run_forever(speed_sp=0) #STOP ACTION
		motorDireita.run_forever(speed_sp=180)
		sleep(0.3)
		x = SensorCorDir.value()
		print(x)
		if x != 'black':
			while(colors[SensorCorDir.value()] == x):
				print("RODANDO PARA A ESQUEDA")
				motorEsquerda.run_forever(speed_sp=0) #STOP ACTION
				motorDireita.run_forever(speed_sp=180)
			sleep(0.1)
			motorDireita.run_forever(speed_sp=0) #STOP ACTION
			sleep(1)
			motorDireita.run_timed(time_sp=1100, speed_sp=-200)
			motorEsquerda.run_timed(time_sp=1100, speed_sp=-200)
			girarRobo(90)
		else: #Fim de pista
			motorDireita.run_forever(speed_sp=-180)
			motorEsquerda.run_forever(speed_sp=-180)
			sleep(0.3)
			motorDireita.run_forever(speed_sp=0) #Roda
			sleep(0.3)
			motorEsquerda.run_forever(speed_sp=0)
			sleep(0.1)


#funcao main -------------------------------------------------------------------
def main():
    btn = Button()
    calibraGyro()
    cor = 0 #none
    Sound.speak('Hello Humans!').wait()
    while not btn.any():
        if colors[SensorCorDir.value()] == 'white' and colors[SensorCorEsq.value()] == 'white':
            andarReto()
            if ultrassonico() and not has_boneco and labyrinth and not plaza:
                agarrarBoneco()#caso way == 0, a funcao troca() eh chamada dentro da funcao agarrarBoneco()
        elif (colors[SensorCorDir.value()] != 'white') or (colors[SensorCorEsq.value()] != 'white') and not plaza: #Condição de saída de pista
    		if (colors[SensorCorDir.value()] == 'none') or (colors[SensorCorDir.value()] == 'black') or (colors[SensorCorEsq.value()] =='none') or (colors[SensorCorEsq.value()] == 'black'):
                sleep(0.2)
                if (colors[SensorCorDir.value()] == 'black') and (colors[SensorCorEsq.value()] =='black'): #Condição Fim de rua (Pós sleep)
    				alinha()
                    cor = 0#caso de rua sem saida: old_color recebe 0 novamente
                    volta()
                elif (colors[SensorCorDir.value()] == 'none') or (colors[SensorCorDir.value()] == 'black') or (colors[SensorCorDir.value()] == 'brown') or (colors[SensorCorEsq.value()] =='none') or (colors[SensorCorEsq.value()] == 'black'):
    				manobra1()
            elif colors[SensorCorDir.value()] != 'white' and colors[SensorCorDir.value()] != 'black' and colors[SensorCorEsq.value()] != 'white' and colors[SensorCorEsq.value()] != 'black':
                old_color = cor #dependemos da cor anterior para saber se a direcao esta correta
                sleep(0.2)
                if colors[SensorCorDir.value()] != 'white' and colors[SensorCorDir.value()] != 'black' and colors[SensorCorEsq.value()] != 'white' and colors[SensorCorEsq.value()] != 'black':
                    alinha()
                    motorDireita.run_timed(time_sp=200, speed_sp=200)
            		motorEsquerda.run_timed(time_sp=200, speed_sp=200)
                    cor = SensorCorDir.value()#NOTE: pegar de um sensor só?
                    if times < number_of_inter:
                        interseccao(old_color, cor)
                    elif times == number_of_inter and labyrinth:
                        rampa()#TODO e NOTE: mudar flag plaza
                    elif times == number_of_inter and not labyrinth:
                        troca()
                        volta()
if __name__ == '__main__':
    main()
