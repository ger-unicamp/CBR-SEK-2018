#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

# definicao de motores
motorDireita = LargeMotor('outB')
motorEsquerda = LargeMotor('outC')
motorGarra = MediumMotor('outA')

# definicao de sensores
ultrassonico = UltrasonicSensor()
assert ultrassonico.connected, "Sensor ultrassonico nao conectado"
ultrassonico.mode = 'US-DIST-CM'

gyro = GyroSensor()
assert gyro.connected, "Giroscopio nao conectado"

sensorCorDir = ColorSensor('in1')
assert sensorCor.connected, "Sensor de cor nao conectado"
sensorCor.mode='COL-COLOR'
colors=('unknown','black','blue','green','yellow','red','white','brown')

sensorCorEsq = ColorSensor('in4')
assert sensorCor2.connected, "Sensor de cor nao conectado"
sensorCor2.mode='COL-COLOR'


def calibraGyro():
	gyro.mode = 'GYRO-RATE'
	sleep(1)
	gyro.mode = 'GYRO-ANG'
	sleep(1)

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
	motorDireita.run_timed(time_sp=600, speed_sp=200)
	motorEsquerda.run_timed(time_sp=600, speed_sp=200)
	sleep(2)
	girarRobo(90)
	sleep(2)
	motorGarra.run_to_rel_pos(position_sp=290, speed_sp=100, stop_action="hold")
	sleep(5)
	motorDireita.run_timed(time_sp=1400, speed_sp=200)
	motorEsquerda.run_timed(time_sp=1400, speed_sp=200)
	sleep(3)
	motorGarra.run_to_rel_pos(position_sp=-300, speed_sp=100, stop_action="hold")
	sleep(5)
	motorDireita.run_timed(time_sp=1400, speed_sp=-200)
	motorEsquerda.run_timed(time_sp=1400, speed_sp=-200)
	sleep(3)
	girarRobo(-90)
calibraGyro()

def manobra1 () #DEFINIR AS VARIAVEIS DOS SENSORES DE COR !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
	motorDireita.stop(stop_action="hold") #Para o robo para executar a manobra
	motorEsquerda.stop(stop_action="hold")
	if (SensorCorDir == none): #confere se o sensor direito está fora da pista
		while(SensorCorEsq != SensorCorDir):
			motorDireita.stop(stop_action="hold")
			motorEsquerda.run_forever(speed_sp=10) #Gira roda esquerda
		motorEsquerda.stop(stop_action="hold") #Para o robo na beirada da pista
		sleep(5)
		motorDireita.run_timed(time_sp=1400, speed_sp=-200) #Retorna ao meio da pista
		motorEsquerda.run_timed(time_sp=1400, speed_sp=-200)
		girarRobo(-90) #Gira para voltar ao percurso
	elif (SensorCorEsq == none): #Tudo igual de maneira antagonica
		while(SensorCorEsq != SensorCorDir):
			motorEsquerda.stop(stop_action="hold")
			motorDireita.run_forever(speed_sp=10)
		motorDireita.stop(stop_action="hold")
		sleep(5)
		motorDireita.run_timed(time_sp=1400, speed_sp=-200)
		motorEsquerda.run_timed(time_sp=1400, speed_sp=-200)
		girarRobo(90)

def manobra2 ():
	if (SensorCorDir == none): #Confere se o sensor de cor direito está fora da pista
		while(SensorCorEsq != SensorCorDir):
			motorDireita.run_forever(speed_sp=50)
			motorEsquerda.run_forever(speed_sp=20) #Diminui a potecia do motor esquedo e retorna à pista
	elif (SensorCorEsq == none):
		while(SensorCorEsq != SensorCorDir):
			motorDireita.run_forever(speed_sp=20)
			motorEsquerda.run_forever(speed_sp=50)


def main():
