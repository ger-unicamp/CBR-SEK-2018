#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

# GER - UNICAMP (30/08/2018)
# SAIDA DO MODULO PLAZA
# ALGORITMO.:
# depois de depositar o boneco no circulo preto
# ira girar 90º para direita e irá até a parede a sua direita (de ré)
# ao encostar na parede o robô irá, gira 90º direita e andar reto até encontrar a parede que contém a saída
# ao encostar na parede o robô irá 90º esquerda e andar reto, até o sensor ultrassônico "enxegar" a saida 
# por fim o robô gira 90º para esquerda e desce a rampa




# -90 GIRAR DIREITA
#  90 GIRAR ESQUERDA



# definicao de motores
motorDireita = LargeMotor('outC')
motorEsquerda = LargeMotor('outB')


# definicao de sensor ultrassonico
ultrassonico = UltrasonicSensor()
assert ultrassonico.connected, "Sensor ultrassonico nao conectado"
ultrassonico.mode = 'US-DIST-CM'

# definicao do sensor giro
def calibraGyro():
    gyro.mode = 'GYRO-RATE'
    sleep(1)
    gyro.mode = 'GYRO-ANG'
    sleep(1)


# funcao: girarRobo
# param: valor do angulo de giro
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

# funcao: saida plaza
def saidaPlaza():
	girarRobo(-90) #girar para direita
	sleep(0.5)
	motorDireita.run_timed(time_sp=1400, speed_sp=-200)  # andar de ré até a parede lateral
    motorEsquerda.run_timed(time_sp=1400, speed_sp=-200)
    girarRobo(-90) #girar para direita
	sleep(0.5)
	motorDireita.run_timed(time_sp=1400, speed_sp=-200)  # andar de ré até a parede frontal
    motorEsquerda.run_timed(time_sp=1400, speed_sp=-200)
    girarRobo(-90) #girar para esquerda
	sleep(0.5)
	
		while(distancia = ultrassonico.value/10 < 5) # enquanto nao "enxergar" a saida continuar andando
			motorDireita.run_forever(speed_sp=50)
            motorEsquerda.run_forever(speed_sp=50)

    # encotrado a saída
    girarRobo(90) #girar para direita
	sleep(0.5)
	motorDireita.run_forever(speed_sp=50)
    motorEsquerda.run_forever(speed_sp=50)



# funcao main para teste
def main ():
	saidaPlaza()