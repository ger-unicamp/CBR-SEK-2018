#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

# definicao de motores
motorDireita = LargeMotor('outC')
motorEsquerda = LargeMotor('outB')
motorGarra = MediumMotor('outA')

# definicao de sensores
ultrassonico = UltrasonicSensor()
assert ultrassonico.connected, "Sensor ultrassonico nao conectado"
ultrassonico.mode = 'US-DIST-CM'

gyro = GyroSensor()
assert gyro.connected, "Giroscopio nao conectado"

SensorCorDir = ColorSensor('in1')
assert SensorCorDir.connected, "Sensor de cor nao conectado"
SensorCorDir.mode='COL-COLOR'
colors=('none','black','blue','green','yellow','red','white','brown')

SensorCorEsq = ColorSensor('in4')
assert SensorCorEsq.connected, "Sensor de cor nao conectado"
SensorCorEsq.mode='COL-COLOR'

while (True):	
	if (colors[SensorCorDir.value()] == 'white' and colors[SensorCorEsq.value()] == 'white'):
		print("estou no branco")
		motorDireita.run_forever(speed_sp=90)
		motorEsquerda.run_forever(speed_sp=90)
	else:
		if (colors[SensorCorDir.value()] == colors[SensorCorEsq.value()]) or (colors[SensorCorDir.value()] == 'green' and colors[SensorCorEsq.value()]== 'blue'):
			print ("cor igual")
			motorDireita.run_forever(speed_sp=90)
			motorEsquerda.run_forever(speed_sp=90)	
		else:
			print ("cor diferente")
			print (colors[SensorCorDir.value()])
			print (colors[SensorCorEsq.value()])
			motorDireita.stop(stop_action="hold")
			motorEsquerda.stop(stop_action="hold")
			sleep(0.5)
			if (colors[SensorCorDir.value()] == 'green' or colors[SensorCorEsq.value()] == 'green':
			    	motorDireita.run_forever(speed_sp=90)
				motorEsquerda.run_forever(speed_sp=90)	
				print ("estou no verde, rampa")
			    	print (colors[SensorCorDir.value()])
				print (colors[SensorCorEsq.value()])
			elif (colors[SensorCorDir.value() == 'blue'] and colors[SensorCorEsq.value()] == 'blue'): # esq  == green
				print ("roda esquerda desalinhada")
				print (colors[SensorCorDir.value()])
				print (colors[SensorCorEsq.value()])
				motorDireita.run_forever(speed_sp=0)
				motorEsquerda.run_forever(speed_sp=90)
			elif (colors[SensorCorDir.value() == 'green'] and colors[SensorCorEsq.value()] == 'blue'):
				print ("roda direita desalinhada")
				print (colors[SensorCorDir.value()])
				print (colors[SensorCorEsq.value()])
				motorDireita.run_forever(speed_sp=90)
				motorEsquerda.run_forever(speed_sp=0)
		
