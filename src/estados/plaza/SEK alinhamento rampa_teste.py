#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

# Connect EV3 color sensor and check connected

# definicao de motores
motorDireita = LargeMotor('outC')
motorEsquerda = LargeMotor('outB')

#definicao dos sensores de cor
sensorCorDir = ColorSensor('in1')
assert sensorCorDir.connected, "Sensor de cor nao conectado"
sensorCorDir.mode='COL-COLOR'

sensorCorEsq = ColorSensor('in4')
assert sensorCorEsq.connected, "Sensor de cor nao conectado"
sensorCorEsq.mode='COL-COLOR'



def rampaIda(): #subida do robo
	print("estou na subida")
	motorDireita.run_forever(speed_sp=0)
	motorEsquerda.run_forever(speed_sp=0)
	sleep(0.5)
	while ((SensorCorDir.value != 2) and (SensorCorEsq.value != 2)):
		motorEsquerda.run_forever(speed_sp=200)
		motorDireita.run_forever(speed_sp=200)
	if (SensorCorDir.value != 2) and (SensorCorEsq.value == 2): # 2 = blue
		print("desalinhado direita baixa")
		while (SensorCorDir.value == 5) and (SensorCorDir.value != 2): # 5 = green
			motorDireita.run_forever(speed_sp=50)
			motorEsquerda.run_forever(speed_sp=0)
		motorDireita.run_forever(speed_sp=0)
		motorEsquerda.run_forever(speed_sp=0)
		sleep(0.5)
	if (SensorCorEsq.value != 2) and (SensorCorDir.value == 2): # 2 = blue
		print("desalinhado esquerda baixa")
		while (SensorCorEsq.value == 5) and (SensorCorEsq.value != 2):  # 5 = green
			motorEsquerda.run_forever(speed_sp=50)
			motorDireita.run_forever(speed_sp=0)
		motorDireita.run_forever(speed_sp=0)
		motorEsquerda.run_forever(speed_sp=0)
		sleep(0.5)
	motorEsquerda.run_forever(speed_sp=200)
	motorDireita.run_forever(speed_sp=200)


def rampaVolta():
	print("estou na descida")
	motorDireita.run_forever(speed_sp=0)
	motorEsquerda.run_forever(speed_sp=0)
	sleep(0.5)
	while ((SensorCorDir.value != 2) and (SensorCorEsq.value != 2)):
		motorEsquerda.run_forever(speed_sp=200)
		motorDireita.run_forever(speed_sp=200)
	if (SensorCorDir.value != 2) and (SensorCorEsq.value == 2): # 2 = blue
		print("desalinhado direita alta")
		motorDireita.run_forever(speed_sp=0)
		motorEsquerda.run_forever(speed_sp=0)
		while (SensorCorDir.value == 3) and (SensorCorDir.value != 2): # 3 = red
			motorDireita.run_forever(speed_sp=50)
			motorEsquerda.run_forever(speed_sp=0)
		motorDireita.run_forever(speed_sp=0)
		motorEsquerda.run_forever(speed_sp=0)
		sleep(0.5)
	if (SensorCorEsq.value != 2) and (SensorCorDir.value == 2): # 2 = blue
		print("desalinhado esquerda alta")
		motorDireita.run_forever(speed_sp=0)
		motorEsquerda.run_forever(speed_sp=0)
		while (SensorCorEsq.value == 3) and (SensorCorEsq.value != 2): # 3 = red
			motorEsquerda.run_forever(speed_sp=50)
			motorDireita.run_forever(speed_sp=0)
		motorDireita.run_forever(speed_sp=0)
		motorEsquerda.run_forever(speed_sp=0)
		sleep(0.5)
	motorEsquerda.run_forever(speed_sp=200)
	motorDireita.run_forever(speed_sp=200)


def andarReto():
	motorEsquerda.run_forever(speed_sp=200)
	motorDireita.run_forever(speed_sp=200)
	


def teste():
	while (True):
		if (SensorCorDir.value == 6) and (SensorCorEsq.value == 6):
			andarReto()
		else:
			rampaIda()

			
teste()
