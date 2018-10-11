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

#DEFINE TAM 30
#DEFINE TAM_MED 15

# inicializar variaveis
none = -1
preto = -1
azul = -1
vermelho = -1
verde = -1
amarelo = -1
branco = -1
marrom = -1


def calibrarCOr(cor):
    listaEsquerda = []
    listaDireito = []

    while i < TAM:
        print('direita'+SensorCorDir.value())
        print('esquerda'+SensorCorEsq.value())
        listaEsquerda.append(SensorCorEsq.value())
        listaDireita.append(SensorCorDir.value())
        i+=1

        # usar valor da mediana
        listaEsquerda.sort
        listaDireita.sort

        # se o valor da mediana dos dois sensores for igual usar o valor
        # se o valor for diferente usar o valor medio
        if(listaEsquerda[TAM_MED] == listaDireita[TAM_MED]):
            cor = listaEsquerda
        else:
            cor = listaEsquerda[TAM] + listaDireita[TAM_MED]/2


def main():
    calibrarCor(azul)
    sleep (0.2)
    print('azul:'+azul)

    calibrarCor(vermelho)
    sleep (0.2)
    print('vermelho:'+vermelho)

    calibrarCor(verde)
    sleep (0.2)
    print('verde:'+verde)

    calibrarCor(amarelo)
    sleep (0.2)
    print('amarelo:'+amarelo)

    calibrarCor(preto)
    sleep (0.2)
    print('preto:'+preto)

    calibrarCor(none)
    sleep (0.2)
    print('none:'+none)

    calibrarCor(amarelo)
    sleep (0.2)

    calibrarCor(branco)
    sleep (0.2)
    print('branco:'branco)

    calibrarCor(marrom)
    sleep (0.2)
    print('marrom:'+marrom)


while(true):
    main

    # testar as cores --
    if(SensorCorDir == azul && SensorCorEsq == azul)
        print('estou na cor azul')

    elif(SensorCorDir == vermelho && SensorCorEsq == vermelho)
        print('estou na cor vermelho')

    elif(SensorCorDir == verde && SensorCorEsq == verde)
        print('estou na cor verde')

    elif(SensorCorDir == branco && SensorCorEsq == branco)
        print('estou na cor branco')

    elif(SensorCorDir == preto && SensorCorEsq == preto)
        print('estou no preto')

    elif(SensorCorDir == amarelo && SensorCorEsq == amarelo)
            print('estou no amarelo')]

    elif(SensorCorDir == none && SensorCorEsq == none)
        print('estou no none')

    print('qualquer cor'+SensorCorDir+SensorCorEsq)
