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

sensorCorDir = ColorSensor('in1')
assert sensorCorDir.connected, "Sensor de cor nao conectado"
sensorCorDir.mode='COL-COLOR'

sensorCorEsq = ColorSensor('in4')
assert sensorCorEsq.connected, "Sensor de cor nao conectado"
sensorCorEsq.mode='COL-COLOR'

# colors=('unknown','black','blue','green','yellow','red','white','brown')

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

def main():#TODO: armazenar infos na pilha 
    btn = Button()
    calibraGyro()
    Sound.speak('Hello Humans!').wait()
    motorDireita.run_forever(speed_sp=200)
    motorEsquerda.run_forever(speed_sp=200)
    while not btn.any():
        if sensorCorDir.value() != 6 and sensorCorEsq.value() != 6:
            if sensorCorDir.value() != 1 and sensorCorEsq.value() != 1:
                motorDireita.run_timed(time_sp=1600, speed_sp=200)
                motorEsquerda.run_timed(time_sp=1600, speed_sp=200)
                sleep(2)
                girarRobo(90)#direita
                motorDireita.run_forever(speed_sp=200)
                motorEsquerda.run_forever(speed_sp=200)
                sleep(4)
            else:
                motorDireita.run_timed(time_sp=1400, speed_sp=-200)
                motorEsquerda.run_timed(time_sp=1400, speed_sp=-200)
                girarRobo(180)#180 ele nao vira bem, vira >180
                motorDireita.run_forever(speed_sp=200)
                motorEsquerda.run_forever(speed_sp=200)
if __name__=="__main__":
    main()
