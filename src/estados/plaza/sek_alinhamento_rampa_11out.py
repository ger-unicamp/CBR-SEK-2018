#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

'''

'''

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

def rampaIda():
    if (colors[SensorCorDir] == "white") and (colors[SensorCorEsq] == "White"):
    	print("estou no branco")
    	sleep(0.2)
	motorDireita.run_forever(speed_sp=90)
	motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir] == "white") and(colors[SensorCorEsq] == "green"):
        print("roda direita desalinhada")
        sleep(0.2)
        motorDireita.run_forever(speed_sp=90)
	motorEsquerda.run_forever(speed_sp=0)
    elif (colors[SensorCorDir] == "green") and (colors[SensorCorEsq] == "White"):
        print("roda esquerda desalinhada")
        sleep(0.2)
        motorDireita.run_forever(speed_sp=0)
	motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir] == "green") and(colors[SensorCorEsq] == "green"):
        print("rodas alinhadas")
        sleep(0.2)
        motorDireita.run_forever(speed_sp=90)
	motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir] == "green") and(colors[SensorCorEsq] == "blue"):
        print("roda direita desalinhada2")
        sleep(0.2)
        motorDireita.run_forever(speed_sp=90)
	motorEsquerda.run_forever(speed_sp=0)
    elif (colors[SensorCorDir] == "blue") and (colors[SensorCorEsq] == "green"):
        print("roda esquerda desalinhada2")
        sleep(0.2)
        motorDireita.run_forever(speed_sp=0)
	motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir] == "blue") and(colors[SensorCorEsq] == "blue"):
        print("rodas alinhadas2")
        sleep(0.2)
        motorDireita.run_forever(speed_sp=90)
	motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir] == "red") or(colors[SensorCorDir] == "red"):
        print("estou no vermelho")
        sleep(0.2)
        motorDireita.run_forever(speed_sp=90)
	motorEsquerda.run_forever(speed_sp=90)

def rampaVolta():
    if (colors[SensorCorDir] == "white") and (colors[SensorCorEsq] == "White"):
    	print("estou no branco")
    	sleep(0.2)
	motorDireita.run_forever(speed_sp=90)
	motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir] == "white") and(colors[SensorCorEsq] == "red"):
        print("roda direita desalinhada")
        sleep(0.2)
        motorDireita.run_forever(speed_sp=90)
	motorEsquerda.run_forever(speed_sp=0)
    elif (colors[SensorCorDir] == "red") and (colors[SensorCorEsq] == "White"):
        print("roda esquerda desalinhada")
        sleep(0.2)
        motorDireita.run_forever(speed_sp=0)
	motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir] == "red") and(colors[SensorCorEsq] == "red"):
        print("rodas alinhadas")
        sleep(0.2)
        motorDireita.run_forever(speed_sp=90)
	motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir] == "red") and(colors[SensorCorEsq] == "blue"):
        print("roda direita desalinhada2")
        sleep(0.2)
        motorDireita.run_forever(speed_sp=90)
	motorEsquerda.run_forever(speed_sp=0)
    elif (colors[SensorCorDir] == "blue") and (colors[SensorCorEsq] == "red"):
        print("roda esquerda desalinhada2")
        sleep(0.2)
        motorDireita.run_forever(speed_sp=0)
	motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir] == "blue") and(colors[SensorCorEsq] == "blue"):
        print("rodas alinhadas2")
        sleep(0.2)
        motorDireita.run_forever(speed_sp=90)
	motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir] == "green") or(colors[SensorCorEsq] == "green"):
        print("estou no verde")
        sleep(0.2)
        motorDireita.run_forever(speed_sp=90)
	motorEsquerda.run_forever(speed_sp=90)    


