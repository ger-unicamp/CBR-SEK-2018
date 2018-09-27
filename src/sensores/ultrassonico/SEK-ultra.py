#!/usr/bin/env python3
# coding=UTF-8
from ev3dev.ev3 import *
from time import sleep

'''
 GER - UNICAMP (27/09/2018)
 SENSOR ULTRASSÔNICO
 ALGORITMO
 Criar uma list de 7 posições que irá armazenar os valores obtidos do sensor ultrassônico
 ordenar essa list, e o valor que será usada para tomar decisões na máquina de estado, seŕa a mediana desta list
'''

# definicao de sensor ultrassonico
ultrassonico = UltrasonicSensor()
assert ultrassonico.connected, "Sensor ultrassonico nao conectado"
ultrassonico.mode = 'US-DIST-CM'

# inicializando list
sensorUltra = []
i = 0


# preenchendo list com os valores do sensor ultrassônico
while(i<10):
    dist = ultrassonico.value()/10
    sensorUltra.append(dist)
    print(sensorUltra)
    i+=1

#ordenação da list
sensorUltra.sort

print(sensorUltra[4]) # impressão das distâncias



