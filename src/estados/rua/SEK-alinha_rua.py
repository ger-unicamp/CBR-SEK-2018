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
			motorDireita.run_forever(speed_sp=-200)
			motorEsquerda.run_forever(speed_sp=200)
			anguloSensor = gyro.value()
	else:
		while(anguloSensor > anguloDesejado + 4): # 4 eh para compensar o lag de leitura do gyro
			motorDireita.run_forever(speed_sp=200)
			motorEsquerda.run_forever(speed_sp=-200)
			anguloSensor = gyro.value()

	motorDireita.stop(stop_action="hold")
	motorEsquerda.stop(stop_action="hold")
	calibraGyro()

def manobra1():
	print("ENTREI NA MANOBRA!! ")
	motorDireita.run_forever(speed_sp=0) #Para o robo para executar a manobra
	motorEsquerda.run_forever(speed_sp=0) #STOP ACTION
	if (colors[SensorCorDir.value()] == 'none') or (colors[SensorCorDir.value()] == 'black') or (colors[SensorCorDir.value()] == 'brown'): #confere se o sensor direito está fora da pista
		while(colors[SensorCorEsq.value()] == 'white'):
			print("RODANDO PARA A DIREITA")
			motorDireita.run_forever(speed_sp=0) #STOP ACTION
			motorEsquerda.run_forever(speed_sp=180) #Gira roda esquerda
		sleep(0.1)
		motorEsquerda.run_forever(speed_sp=0) #Para o robo na beirada da pista #STOP ACTION
		sleep(1)
		motorDireita.run_timed(time_sp=1100, speed_sp=-200) #Retorna ao meio da pista
		motorEsquerda.run_timed(time_sp=1100, speed_sp=-200)
		girarRobo(-90) #Gira para voltar ao percurso
	elif (colors[SensorCorEsq.value()] == 'none') or (colors[SensorCorEsq.value()] == 'black') or (colors[SensorCorEsq.value()] == 'brown'): #Tudo igual de maneira antagonica
		while(colors[SensorCorDir.value()] == 'white'):
			print("RODANDO PARA A ESQUEDA")
			motorEsquerda.run_forever(speed_sp=0) #STOP ACTION
			motorDireita.run_forever(speed_sp=180)
		sleep(0.1)
		motorDireita.run_forever(speed_sp=0) #STOP ACTION
		sleep(1)
		motorDireita.run_timed(time_sp=1100, speed_sp=-200)
		motorEsquerda.run_timed(time_sp=1100, speed_sp=-200)
		girarRobo(90)

def alinha1(): #Começar função alinha com StopMotion
	motorEsquerda.run_forever(speed_sp=0)
	motorDireita.run_forever(speed_sp=0)
	sleep(0.4)
	while(colors[SensorCorDir.value()] != 'white') or (colors[SensorCorEsq.value()] != 'white'):
		motorDireita.run_forever(speed_sp=-100)
		motorEsquerda.run_forever(speed_sp=-100)
	if(colors[SensorCorDir.value()] == 'white'):
		while (colors[SensorCorEsq.value()] != 'white'):
			motorDireita.run_forever(speed_sp=0) #STOP ACTION
			motorEsquerda.run_forever(speed_sp=-180)
	elif(colors[SensorCorEsq.value()] == 'white'):
		while (colors[SensorCorDir.value()] != 'white'):
			motorDireita.run_forever(speed_sp=-180) #STOP ACTION
			motorEsquerda.run_forever(speed_sp=0)
	motorEsquerda.run_forever(speed_sp=0)
	motorDireita.run_forever(speed_sp=0)
	exit()

def alinha():
	motorEsquerda.run_forever(speed_sp=0)
	motorDireita.run_forever(speed_sp=0)
	while(colors[SensorCorDir.value()] != 'white') and (colors[SensorCorEsq.value()] != 'white'):
		if(colors[SensorCorDir.value()] != 'white'):
			motorDireita.run_forever(speed_sp=-50)
		else:
			motorDireita.run_forever(speed_sp=0)
		if(colors[SensorCorEsq.value()] != 'white'):
			motorEsquerda.run_forever(speed_sp=-50)
		else:
			motorEsquerda.run_forever(speed_sp=0)
	motorEsquerda.run_forever(speed_sp=0)
	motorDireita.run_forever(speed_sp=0)
	exit()

def main(): #TESTES
	motorEsquerda.run_forever(speed_sp=200)
	motorDireita.run_forever(speed_sp=200)
	print("Sensor direito:", colors[SensorCorDir.value()])
	print("Sensor esquerdo:", colors[SensorCorEsq.value()])
	if (colors[SensorCorDir.value()] != 'white') or (colors[SensorCorEsq.value()] != 'white'):
		if (colors[SensorCorDir.value()] == 'none') or (colors[SensorCorDir.value()] == 'black') or (colors[SensorCorEsq.value()] =='none') or (colors[SensorCorEsq.value()] == 'black'): #verificação Final da RUA
			sleep(0.2)
			if (colors[SensorCorDir.value()] == 'black') and (colors[SensorCorEsq.value()] =='black'):
				print("FIM DA RUA")
				alinha()
			elif (colors[SensorCorDir.value()] == 'none') or (colors[SensorCorDir.value()] == 'black') or (colors[SensorCorDir.value()] == 'brown') or (colors[SensorCorEsq.value()] =='none') or (colors[SensorCorEsq.value()] == 'black'):
				print("BORA PRA MANOBRA")
				manobra1()
		elif (colors[SensorCorDir.value()] == 'yellow') or (colors[SensorCorEsq.value()] =='yellow'):
			sleep(0.2)
			if (colors[SensorCorDir.value()] == 'yellow') and (colors[SensorCorEsq.value()] =='yellow'):
				alinha()
		elif (colors[SensorCorDir.value()] == 'red') or (colors[SensorCorEsq.value()] =='red'):
			sleep(0.2)
			if (colors[SensorCorDir.value()] == 'red') and (colors[SensorCorEsq.value()] =='red'):
				alinha()
		elif (colors[SensorCorDir.value()] == 'green') or (colors[SensorCorEsq.value()] =='green'):
			sleep(0.2)
			if (colors[SensorCorDir.value()] == 'green') and (colors[SensorCorEsq.value()] =='green'):
				alinha()



while(True):
	main()
