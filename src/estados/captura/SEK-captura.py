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

#variaveis globais
has_boneco = False#variavel de verificacao para pegar ou nao bonecos

gyro = GyroSensor()
assert gyro.connected, "Giroscopio nao conectado"

sensorCor = ColorSensor()
assert sensorCor.connected, "Sensor de cor nao conectado"
sensorCor.mode='COL-COLOR'
colors=('unknown','black','blue','green','yellow','red','white','brown')

def calibraGyro():
    gyro.mode = 'GYRO-RATE'
    sleep(1)
    gyro.mode = 'GYRO-ANG'
    sleep(1)

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

def agarrarBoneco(distancia):
    global has_boneco
    motorDireita.run_timed(time_sp=500, speed_sp=200)
    motorEsquerda.run_timed(time_sp=500, speed_sp=200)
    sleep(2)
    girarRobo(90)
    motorGarra.run_to_rel_pos(position_sp=290, speed_sp=100, stop_action="hold")
    sleep(2)
    motorDireita.run_forever(speed_sp=170)
    motorEsquerda.run_forever(speed_sp=170)
    sleep(distancia/10)
    motorDireita.stop(stop_action="hold")
    motorEsquerda.stop(stop_action="hold")
    motorGarra.run_to_rel_pos(position_sp=-290, speed_sp=100, stop_action="hold")
    #de -100 a -330 a garra n subiu
    sleep(1)
    #como subir a garra?
    # motorDireita.run_timed(time_sp=1400, speed_sp=-200)
    # motorEsquerda.run_timed(time_sp=1400, speed_sp=-200)
    motorDireita.run_forever(speed_sp=-170)
    motorEsquerda.run_forever(speed_sp=-170)
    sleep(distancia/10)
    motorDireita.stop(stop_action="hold")
    motorEsquerda.stop(stop_action="hold")
    girarRobo(-90)
    has_boneco = True
    calibraGyro()

def main():
    btn = Button()
    calibraGyro()
    Sound.speak('Hello Humans!').wait()
    motorGarra.run_to_rel_pos(position_sp=190, speed_sp=100, stop_action="hold")
    sleep(2)
    # motorGarra.run_to_rel_pos(position_sp=-200, speed_sp=100, stop_action="hold")
    sleep(2)
    # motorDireita.run_forever(speed_sp=150)
    # motorEsquerda.run_forever(speed_sp=150)
    sleep(0.7)
    global has_boneco
    # while not btn.any():
    #     distancia = [ultrassonico.value()/10 for i in range(10)]# converte de mm para cm
    #     distancia.sort()
    #     if(distancia[4] < 25 and not has_boneco):
    #         print('distancia lida pelo ultrassonico: {}'.format(distancia[4]))
    #         motorDireita.stop(stop_action="hold")
    #         motorEsquerda.stop(stop_action="hold")
    #         sleep(0.5)
    #         agarrarBoneco(distancia[4])
    #         break
    #     else:
    #         motorDireita.run_forever(speed_sp=200)
    #         motorEsquerda.run_forever(speed_sp=200)
    motorDireita.stop(stop_action="hold")
    motorEsquerda.stop(stop_action="hold")

if __name__ == "__main__":
    main()
