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
    if (colors[SensorCorDir] == "white") and (colors[SensorCorEsq] == "White"):
    	print("estou no branco")
	motorDireita.run_forever(speed_sp=90)
	motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir] == "white") and(colors[SensorCorDir] == "green"):
        print("roda direita desalinhada")
        motorDireita.run_forever(speed_sp=90)
	motorEsquerda.run_forever(speed_sp=0)
    elif (colors[SensorCorDir] == "green") and (colors[SensorCorEsq] == "White"):
        print("roda esquerda desalinhada")
        motorDireita.run_forever(speed_sp=0)
	motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir] == "green") and(colors[SensorCorDir] == "green"):
        print("rodas alinhadas")
        motorDireita.run_forever(speed_sp=90)
	motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir] == "green") and(colors[SensorCorDir] == "blue"):
        print("roda direita desalinhada2")
        motorDireita.run_forever(speed_sp=90)
	motorEsquerda.run_forever(speed_sp=0)
    elif (colors[SensorCorDir] == "blue") and (colors[SensorCorEsq] == "green"):
        print("roda esquerda desalinhada2")
        motorDireita.run_forever(speed_sp=0)
	motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir] == "blue") and(colors[SensorCorDir] == "blue"):
        print("rodas alinhadas2")
        motorDireita.run_forever(speed_sp=90)
	motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir] == "red") or(colors[SensorCorDir] == "red"):
        print("estou no vermelho")
        motorDireita.run_forever(speed_sp=90)
	motorEsquerda.run_forever(speed_sp=90)






    
