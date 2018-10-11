#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

# Connect EV3 color sensor and check connected.

SensorCorDir = ColorSensor('in1')
assert SensorCorDir.connected, "Sensor de cor nao conectado"
SensorCorDir.mode='COL-AMBIENT'
#colors=('none','black','blue','green','yellow','red','white','brown')

SensorCorEsq = ColorSensor('in4')
assert SensorCorEsq.connected, "Sensor de cor nao conectado"
SensorCorEsq.mode='COL-AMBIENT'

azul = -1
vermelho = -1
verde = -1
amarelo = -1



def calibrarCOr(cor):
    listaEsquerda = []
    listaDireito = []

    while True:
        print('direita'+SensorCorDir.value())
        print('esquerda'+SensorCorEsq.value())


        for i in 20:
            listaEsquerda.append(SensorCorEsq.value())
            listaDireita = append(SensorCorDir.value())
            i+=1

        listaEsquerda.sort
        listaDireita.sort

        if(listaEsquerda[10] == listaDireita[10]):
            cor = listaEsquerda
        else:
            cor = listaEsquerda[10] + listaDireita[10]/2


def main():
    calibrarCor(azul)
    sleep (0.2)

    calibrarCor(vermelho)
    sleep (0.2)

    calibrarCor(verde)
    sleep (0.2)

    calibrarCor(amarelo)
    sleep (0.2)

    print('azul:'+azul+'-- vermelho:'+vermelho+'-- verde:'+verde+'-- amarelo:'+amarelo);


while(true):
    main