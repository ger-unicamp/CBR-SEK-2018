#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep
from interseccao.py import Interseccao

#variaveis globais e flags------------------------------------------------------
colors=('none','black','blue','green','yellow','red','white','brown')
has_boneco = False#variavel de verificacao para pegar ou nao bonecos
labyrinth = False#para saber quando ja conhecemos o laribirinto (1a vez apenas)
#path = list() #lista com as direcoes a serem seguidas pelo trajeto (path)
number_of_inter = 4 # na FINAL trocar por 6
times = 0 #quantidade de interseccoes passadas times pertence ao intervalo [0,number_of_inter]
way = 1 #1 se for ida (direto) ao setido do plaza, 0 se for volta (contrario) ao sentido do plaza
inter = Interseccao()
plaza = False

# definicao de motores----------------------------------------------------------
motorDireita = LargeMotor('outC')
motorEsquerda = LargeMotor('outB')
motorGarra = MediumMotor('outA')

# definicao de sensores---------------------------------------------------------
ultrassonico = UltrasonicSensor()
assert ultrassonico.connected, "Sensor ultrassonico nao conectado"
ultrassonico.mode = 'US-DIST-CM'

SensorCorDir = ColorSensor('in1')
assert SensorCorDir.connected, "Sensor de cor nao conectado"
SensorCorDir.mode='COL-COLOR'

SensorCorEsq = ColorSensor('in4')
assert SensorCorEsq.connected, "Sensor de cor nao conectado"
SensorCorEsq.mode='COL-COLOR'

gyro = GyroSensor()
assert gyro.connected, "Giroscopio nao conectado"

#funcoes (e estados) -------------------------------------------------------------
def calibraGyro():
    gyro.mode = 'GYRO-RATE'
    sleep(1)
    gyro.mode = 'GYRO-ANG'
    sleep(1)
def troca():#NOTE: trocar direcoes das cores
    if way ==1: way=0
    else: way=1
    if times==number_of_inter and not labyrinth: labyrinth=True
def ultrassonico():
    aux = [ultrassonico.value()/10 for i in range(10)]
    aux.sort()
    if aux[4] < 20: return True
    else: return False
def girarRobo(anguloDesejado):
    calibraGyro()
    anguloSensor = gyro.value()
    if(anguloDesejado > 0):
        while(anguloSensor < anguloDesejado - 4): # 4 eh para compensar o lag de leitura do gyro
            motorDireita.run_forever(speed_sp=-50)
            motorEsquerda.run_forever(speed_sp=50)
            anguloSensor = gyro.value()
    else:
        while(anguloSensor > anguloDesejado + 4): # 4 eh para compensar o lag de leitura do gyro
            motorDireita.run_forever(speed_sp=50)
            motorEsquerda.run_forever(speed_sp=-50)
            anguloSensor = gyro.value()

    motorDireita.stop(stop_action="hold")
    motorEsquerda.stop(stop_action="hold")
    calibraGyro()
def agarrarBoneco():
    motorDireita.run_timed(time_sp=500, speed_sp=200)
    motorEsquerda.run_timed(time_sp=500, speed_sp=200)
    sleep(2)
    girarRobo(90)
    sleep(2)
    motorGarra.run_to_rel_pos(position_sp=290, speed_sp=100, stop_action="hold")
    sleep(5)
    motorDireita.run_timed(time_sp=1400, speed_sp=200)
    motorEsquerda.run_timed(time_sp=1400, speed_sp=200)
    sleep(3)
    motorGarra.run_to_rel_pos(position_sp=-290, speed_sp=100, stop_action="hold")#NOTE: TESTAR GARRAS
    #de -100 a -330 a garra n subiu
    sleep(5)
    #como subir a garra?
    motorDireita.run_timed(time_sp=1400, speed_sp=-200)
    motorEsquerda.run_timed(time_sp=1400, speed_sp=-200)
    sleep(3)
    girarRobo(-90)
    has_boneco = True
    calibraGyro()
def andarReto():
    motorDireita.run_forever(speed_sp=200)
    motorEsquerda.run_forever(speed_sp=200)
def volta():
    motorDireita.run_timed(time_sp=800 speed_sp=-200)
    motorEsquerda.run_timed(time_sp=800 speed_sp=-200)
    girarRobo(90)
    girarRobo(90)
    andarReto()

#funcao main -------------------------------------------------------------------
def main():
    btn = Button()
    calibraGyro()
    Sound.speak('Hello Humans!').wait()
    while not btn.any():
        if colors(SensorCorDir.value()) == 'white' and colors(SensorCorEsq.value()) == 'white':
            andarReto()#NOTE: VAI RODAR TODA VEZ QUE ESTIVER EM BRANCO?
            if ultrassonico() and not has_boneco and labyrinth:
                agarrarBoneco()
                troca()
        elif (colors(SensorCorDir.value()) == 'white' and colors(SensorCorEsq.value()) == 'black') or (colors(SensorCorDir.value()) == 'black' and colors(SensorCorEsq.value()) == 'white'):#NOTE: botar none e brown
            alinhaRua()#TODO
        elif colors(SensorCorDir.value()) != 'white' and colors(SensorCorDir.value()) != 'black' and colors(SensorCorEsq.value()) != 'white' and colors(SensorCorEsq.value()) != 'black':
            if times < number_of_inter:
                interseccao()#TODO
            elif times == number_of_inter and labyrinth:
                rampa()#TODO e NOTE: mudar flag plaza
            elif times == number_of_inter and not labyrinth:
                troca()#NOTE:botar a volta
                volta()
        elif colors(SensorCorDir.value()) == 'black' and colors(SensorCorEsq.value()) == 'black':
            volta()
if __name__ == '__main__':
    main()
