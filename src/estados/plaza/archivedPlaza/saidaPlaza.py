#!/usr/bin/env python3
# coding=UTF-8
from ev3dev.ev3 import *
from time import sleep

'''
 GER - UNICAMP (30/08/2018)
 SAIDA DO MODULO PLAZA
 ALGORITMO.:
 depois de depositar o boneco no circulo preto
 ira girar 90º para direita e irá até a parede a sua direita (de ré)
 ao encostar na parede o robô irá, gira 90º direita e andar reto até encontrar a parede que contém a saída
 ao encostar na parede o robô irá 90º esquerda e andar reto, até o sensor ultrassônico "enxegar" a saida 
 por fim o robô gira 90º para esquerda e desce a rampa

  90 GIRAR DIREITA
  -90 GIRAR ESQUERDA
'''

TAM = 30
TAM_MED = 15
ANDAR_PLAZA = 300000

# definicao de motores
motorDireita = LargeMotor('outC')
motorEsquerdo = LargeMotor('outB')


# definicao de sensor ultrassonico
ultrassonico = UltrasonicSensor()
assert ultrassonico.connected, "Sensor ultrassonico nao conectado"
ultrassonico.mode = 'US-DIST-CM'

gyro = GyroSensor()
assert gyro.connected, "Giroscopio nao conectado"

# definicao do sensor giro
def calibraGyro():
    gyro.mode = 'GYRO-RATE'
    sleep(1)
    gyro.mode = 'GYRO-ANG'
    sleep(1)



# funcao: sensor ultrassônico
# param: nenhum
# retunr: valor da mediana da list preenchendo pelo sensor
def ultraSensor():
    sensorUltra = [] # inicializando list
    i = 0

    while(i < TAM):  # preenchendo list com os valores do sensor ultrassônico
        dist = ultrassonico.value()/10
        sensorUltra.append(dist)
        #print(sensorUltra)
        i+=1

    sensorUltra.sort  #ordenação da list
    return sensorUltra[TAM_MED]



# funcao: girarRobo
# param: valor do angulo de giro
def girarRobo(anguloDesejado):
	calibraGyro()
	anguloSensor = gyro.value()

	if(anguloDesejado > 0):
		while(anguloSensor < anguloDesejado - 4): # 4 eh para compensar o lag de leitura do gyro
			motorDireita.run_forever(speed_sp=0)
			motorEsquerdo.run_forever(speed_sp=250)
			anguloSensor = gyro.value()
	else:
		while(anguloSensor > anguloDesejado + 4): # 4 eh para compensar o lag de leitura do gyro
			motorDireita.run_forever(speed_sp=250)
			motorEsquerdo.run_forever(speed_sp=0)
			anguloSensor = gyro.value()


calibraGyro()

# funcao: saida plaza
def saidaPlaza():
 
    print("GIROU PARA DIREITA 1")
    girarRobo(-90) #girar para esquerda
    sleep(0.5)
 
    print("ANDAR PARA FRENTE DURANTE X TEMPO 1")
    motorDireita.run_timed(time_sp=ANDAR_PLAZA, speed_sp=250)  # andar de ate a parede lateral
    motorEsquerdo.run_timed(time_sp=ANDAR_PLAZA, speed_sp=250)
   
    print("VOU GIRAR PARA DIREITA 2")
    girarRobo(-90) #girar para esquerda
    sleep(0.5)
 
    print("ANDAR PARA FRENTE DURANTE X TEMPO 2")
    motorDireita.run_timed(time_sp=ANDAR_PLAZA, speed_sp=250)  # andar de ate a parede frontal
    motorEsquerdo.run_timed(time_sp=ANDAR_PLAZA, speed_sp=250)

    girarRobo(-90) #girar para esquerda
    sleep(0.5)
	
    print("PROCURANDO A SAIDA")
    while(ultraSensor() < 10): # enquanto nao "enxergar" a saida continuar andando
	    motorEsquerdo.run_forever(speed_sp=50)
	    motorDireita.run_forever(speed_sp=50)

    print("ACHEI A SAIDA")
    # encotrado a saida
    sleep(0.5)
    girarRobo(90) #girar para direita
    sleep(0.5)
    motorDireita.run_forever(speed_sp=50)
    motorEsquerdo.run_forever(speed_sp=50)




# funcao main para teste
def main ():
    print("CHAMAO A FUNCAO SAIDA PLAZA")
    saidaPlaza()
    exit()

while(True):
    main()