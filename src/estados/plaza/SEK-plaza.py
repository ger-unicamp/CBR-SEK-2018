#!/usr/bin/env python3
from ev3dev.ev3 import *
from time import sleep

# definicao de motores
motorDireita = LargeMotor('outB')
motorEsquerda = LargeMotor('outC')
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

def plaza_entrega_boneco ():
	#Entrega do boneco
	while (colors[SensorCorDir.value()] != "black") and (colors[SensorCorEsq.value()] != "black"):
		motorDireita.run_forever(speed_sp=50)
		motorEsquerda.run_forever(speed_sp=50)
	sleep(1) #Esse sleep serve para não ficar na borda do centro preto
	motorDireita.stop(stop_action="hold")
	motorEsquerda.stop(stop_action="hold")
	motorGarra.run_to_rel_pos(position_sp=290, speed_sp=100, stop_action="hold") #abre H ra
	motorDireita.run_timed(time_sp=1400, speed_sp=-50)
	motorEsquerda.run_timed(time_sp=1400, speed_sp=-50)
	sleep(3)
	motorGarra.run_to_rel_pos(position_sp=-300, speed_sp=100, stop_action="hold") #fecha H ra

def plaza_modo1():
	giraRobo (180)
	motorDireita.run_timed(time_sp=2000, speed_sp=200)
	motorEsquerda.run_timed(time_sp=2000, speed_sp=200)
	motorDireita.stop(stop_action="hold")
	motorEsquerda.stop(stop_action="hold")
	#Verifica distancia das paredes:
	dist_esq = UltrasonicSensor()
	giraRobo (180)
	dist_dir = UltrasonicSensor()
	girarRobo (180)
	if (dist_esq - dist_dir < 3):
		motorDireita.run_timed(time_sp=2000, speed_sp=200)
		motorEsquerda.run_timed(time_sp=2000, speed_sp=200)



def main():
	while (True):
		print ("Hello")
		sleep(0.1)
		motorDireita.run_forever(speed_sp=50)
		motorEsquerda.run_forever(speed_sp=50)
		sleep(1)
		if (colors[SensorCorDir.value()] == "red") or (colors[SensorCorEsq.value()] != "red"):
			plaza_entrega_boneco()
			plaza_modo1()
