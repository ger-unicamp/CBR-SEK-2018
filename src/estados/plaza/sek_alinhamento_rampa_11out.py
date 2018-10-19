#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

'''
#
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

tempo = 0.1
local = " "
localant = " "

def rampaIda():
    if (colors[SensorCorDir.value()] == "white") and (colors[SensorCorEsq.value()] == "white"):
        print("estou no branco")
        local = "estou no branco"
        if local != localant:
            motorDireita.run_forever(speed_sp=0)
            motorEsquerda.run_forever(speed_sp=0)            
            sleep(0.5)
        sleep(tempo)
        motorDireita.run_forever(speed_sp=90)
        motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir.value()] == "white") and(colors[SensorCorEsq.value()] == "green"):
        print("roda direita desalinhada")
        local = "roda direita desalinhada"
        if local != localant:
            motorDireita.run_forever(speed_sp=0)
            motorEsquerda.run_forever(speed_sp=0)            
            sleep(0.5)
        sleep(tempo)
        motorDireita.run_forever(speed_sp=90)
        motorEsquerda.run_forever(speed_sp=0)
    elif (colors[SensorCorDir.value()] == "green") and (colors[SensorCorEsq.value()] == "white"):
        print("roda esquerda desalinhada")
        local = "roda esquerda desalinhada"
        if local != localant:
            motorDireita.run_forever(speed_sp=0)
            motorEsquerda.run_forever(speed_sp=0)            
            sleep(0.5)
        sleep(tempo)
        motorDireita.run_forever(speed_sp=0)
        motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir.value()] == "green") and(colors[SensorCorEsq.value()] == "green"):
        print("rodas alinhadas")
        local = "rodas alinhadas"
        if local != localant:
            motorDireita.run_forever(speed_sp=0)
            motorEsquerda.run_forever(speed_sp=0)            
            sleep(0.5)
        sleep(tempo)
        motorDireita.run_forever(speed_sp=90)
        motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir.value()] == "green") and(colors[SensorCorEsq.value()] == "blue"):
        print("roda direita desalinhada2")
        local = "roda direita desalinhada2"
        if local != localant:
            motorDireita.run_forever(speed_sp=0)
            motorEsquerda.run_forever(speed_sp=0)            
            sleep(0.5)
        sleep(tempo)
        motorDireita.run_forever(speed_sp=90)
        motorEsquerda.run_forever(speed_sp=0)
    elif (colors[SensorCorDir.value()] == "blue") and (colors[SensorCorEsq.value()] == "green"):
        print("roda esquerda desalinhada2")
        local = "roda esquerda desalinhada2"
        if local != localant:
            motorDireita.run_forever(speed_sp=0)
            motorEsquerda.run_forever(speed_sp=0)            
            sleep(0.5)
        sleep(tempo)
        motorDireita.run_forever(speed_sp=0)
        motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir.value()] == "blue") and(colors[SensorCorEsq.value()] == "blue"):
        print("rodas alinhadas2")
        local = "rodas alinhadas2"
        if local != localant:
            motorDireita.run_forever(speed_sp=0)
            motorEsquerda.run_forever(speed_sp=0)            
            sleep(0.5)
        sleep(tempo)
        motorDireita.run_forever(speed_sp=90)
        motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir.value()] == "red") or(colors[SensorCorDir.value()] == "red"):
        print("estou no vermelho")
        local = "estou no vermelho"
        if local != localant:
            motorDireita.run_forever(speed_sp=0)
            motorEsquerda.run_forever(speed_sp=0)            
            sleep(0.5)
        sleep(tempo)
        motorDireita.run_forever(speed_sp=90)
        motorEsquerda.run_forever(speed_sp=90)
    localant = local

def rampaVolta():
    if (colors[SensorCorDir.value()] == "white") and (colors[SensorCorEsq.value()] == "white"):
        print("estou no branco")
        sleep(tempo)
        motorDireita.run_forever(speed_sp=90)
        motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir.value()] == "white") and(colors[SensorCorEsq.value()] == "red"):
        print("roda direita desalinhada")
        sleep(tempo)
        motorDireita.run_forever(speed_sp=90)
        motorEsquerda.run_forever(speed_sp=0)
    elif (colors[SensorCorDir.value()] == "red") and (colors[SensorCorEsq.value()] == "white"):
        print("roda esquerda desalinhada")
        sleep(tempo)
        motorDireita.run_forever(speed_sp=0)
        motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir.value()] == "red") and(colors[SensorCorEsq.value()] == "red"):
        print("rodas alinhadas")
        sleep(tempo)
        motorDireita.run_forever(speed_sp=90)
        motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir.value()] == "red") and(colors[SensorCorEsq].value() == "blue"):
        print("roda direita desalinhada2")
        sleep(tempo)
        motorDireita.run_forever(speed_sp=90)
        motorEsquerda.run_forever(speed_sp=0)
    elif (colors[SensorCorDir.value()] == "blue") and (colors[SensorCorEsq.value()] == "red"):
        print("roda esquerda desalinhada2")
        sleep(tempo)
        motorDireita.run_forever(speed_sp=0)
        motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir.value()] == "blue") and(colors[SensorCorEsq.value()] == "blue"):
        print("rodas alinhadas2")
        sleep(tempo)
        motorDireita.run_forever(speed_sp=90)
        motorEsquerda.run_forever(speed_sp=90)
    elif (colors[SensorCorDir.value()] == "green") or(colors[SensorCorEsq.value()] == "green"):
        print("estou no verde")
        sleep(tempo)
        motorDireita.run_forever(speed_sp=90)
        motorEsquerda.run_forever(speed_sp=90)    

while(True):
    rampaIda()

