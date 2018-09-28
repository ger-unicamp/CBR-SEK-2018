#!/usr/bin/env python3
# coding=UTF-8
from ev3dev.ev3 import *
from time import sleep

# Connect EV3 color sensor and check connected

# definicao de motores
motorDireita = LargeMotor('outC')
motorEsquerda = LargeMotor('outB')
motorGarra = MediumMotor('outA')

#definicao dos sensores de cor
SensorCorDir = ColorSensor('in1')
assert SensorCorDir.connected, "Sensor de cor nao conectado"
SensorCorDir.mode='COL-COLOR'
colors=('none','black','blue','green','yellow','red','white','brown')

SensorCorEsq = ColorSensor('in4')
assert SensorCorEsq.connected, "Sensor de cor nao conectado"
SensorCorEsq.mode='COL-COLOR'


def rampaIda():
	print('funciona aqui 0001')
	while (colors[SensorCorEsq.value()] == 'white' or colors[SensorCorDir.value()] == 'white'):
		motorDireita.run_forever(speed_sp=50)
		motorEsquerda.run_forever(speed_sp=50)

	print('funciona aqui 0002')
	while (colors[SensorCorEsq.value()] != 'blue' or colors[SensorCorDir.value()] != 'blue'):
		print('nao esta alinhado no azul -- vermelho ou verde')
		print(colors[SensorCorEsq.value()]) 
	
		while colors[SensorCorEsq.value()] == 'red' or colors[SensorCorDir.value()] == 'green':
			print(colors[SensorCorEsq.value()]+'CORRIGIR - ESQUERDO(VERMELHO) ou DIREITO(VERDE)')
			motorEsquerdo.run_time(time_sp=200, speed_sp=5)
			motorDireita.run_time(time_sp=200, speed_sp=-5)

		while colors[SensorCorDir.value()] == 'red' or colors[SensorCorEsq.value()] == 'green':
			print(colors[SensorCorEsq.value()]+'CORRIGIR - DIREITO(VERMELHOo) ou ESQUERDO(VERDE)')
			motorEsquerdo.run_time(time_sp=200, speed_sp=-5)
			motorDireita.run_time(time_sp=200, speed_sp=5)
	
	sleep(2)
	motorDireita.run_forever(speed_sp=50)
	motorEsquerda.run_forever(speed_sp=50)


while(True):

	rampaIda()
	print('estou aqui 01')
