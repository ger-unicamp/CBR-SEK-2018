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
		if (colors[SensorCorDir.value()] == colors[SensorCorEsq.value()]):
			motorDireita.run_forever(speed_sp=90)
			motorEsquerda.run_forever(speed_sp=90)	
		else:
			motorDireita.stop(stop_action="hold")
			motorEsquerda.stop(stop_action="hold")
			sleep(0.5)
			while (colors[SensorCorDir.value() == 'green'] and colors[SensorCorEsq.value()] == 'white'):
				motorDireita.run_forever(speed_sp=0)
				motorEsquerda.run_forever(speed_sp=90)
			while (colors[SensorCorDir.value() == 'white'] and colors[SensorCorEsq.value()] == 'green'):
				motorDireita.run_forever(speed_sp=90)
				motorEsquerda.run_forever(speed_sp=0)
			motorDireita.stop(stop_action="hold")
			motorEsquerda.stop(stop_action="hold")
		
