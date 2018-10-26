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

def manobraextra():
	print("ENTREI NA MANOBRA!! ")
	motorDireita.run_forever(speed_sp=0) #Para o robo para executar a manobra
	motorEsquerda.run_forever(speed_sp=0) #STOP ACTION
	if (colors[SensorCorDir.value()] == 'none') or (colors[SensorCorDir.value()] == 'black') or (colors[SensorCorDir.value()] == 'brown'): #confere se o sensor direito está fora da pista
		motorDireita.run_forever(speed_sp=0) #STOP ACTION
		motorEsquerda.run_forever(speed_sp=180) #Gira roda esquerda
		sleep(1.13)
		x = colors[SensorCorEsq.value()]
		print(x)
		if x != 'black':
			while(colors[SensorCorEsq.value()] == x):
				#print("RODANDO PARA A DIREITA")
				motorDireita.run_forever(speed_sp=0) #STOP ACTION
				motorEsquerda.run_forever(speed_sp=180) #Gira roda esquerda
			sleep(0.1)
			motorEsquerda.run_forever(speed_sp=0) #Para o robo na beirada da pista #STOP ACTION
			sleep(1)
			motorDireita.run_timed(time_sp=1100, speed_sp=-200) #Retorna ao meio da pista
			motorEsquerda.run_timed(time_sp=1100, speed_sp=-200)
			girarRobo(-90) #Gira para voltar ao percurso
		else: #Fim de pista
			motorDireita.run_forever(speed_sp=-150)
			motorEsquerda.run_forever(speed_sp=0)
			sleep(1.5)
			while(colors[SensorCorDir.value()] != 'black'):
				motorDireita.run_forever(speed_sp=-150)
			motorEsquerda.run_forever(speed_sp=0)
			while(colors[SensorCorDir.value()] != 'black') or (colors[SensorCorEsq.value()] != 'black'):
				if(colors[SensorCorDir.value()] != 'black'): #Enquanto os dois não estiverem fora da interssecção ou fora do fim de pista, alinha os dois sensores
					motorDireita.run_forever(speed_sp=-150) #em branco
				else:
					motorDireita.run_forever(speed_sp=0)
				if(colors[SensorCorEsq.value()] != 'black'):
					motorEsquerda.run_forever(speed_sp=-150)
				else:
					motorEsquerda.run_forever(speed_sp=0)
			motorEsquerda.run_forever(speed_sp=0)
			motorDireita.run_forever(speed_sp=0)

	elif (colors[SensorCorEsq.value()] == 'none') or (colors[SensorCorEsq.value()] == 'black') or (colors[SensorCorEsq.value()] == 'brown'): #Tudo igual de maneira antagonica
		motorEsquerda.run_forever(speed_sp=0) #STOP ACTION
		motorDireita.run_forever(speed_sp=180)
		sleep(1.13)
		x = colors[SensorCorDir.value()]
		print(x)
		if x != 'black':
			while(colors[SensorCorDir.value()] == x):
				#print("RODANDO PARA A ESQUEDA")
				motorEsquerda.run_forever(speed_sp=0) #STOP ACTION
				motorDireita.run_forever(speed_sp=180)
			sleep(0.1)
			motorDireita.run_forever(speed_sp=0) #STOP ACTION
			sleep(1)
			motorDireita.run_timed(time_sp=1100, speed_sp=-200)
			motorEsquerda.run_timed(time_sp=1100, speed_sp=-200)
			girarRobo(90)
		else: #Fim de pista
			motorDireita.run_forever(speed_sp=0)
			motorEsquerda.run_forever(speed_sp=-150)
			sleep(1.5)
			while(colors[SensorCorEsq.value()] != 'black'):
				motorEsquerda.run_forever(speed_sp=-150)
			motorEsquerda.run_forever(speed_sp=0)
			while(colors[SensorCorDir.value()] != 'black') or (colors[SensorCorEsq.value()] != 'black'):
				if(colors[SensorCorDir.value()] != 'black'): #Enquanto os dois não estiverem fora da interssecção ou fora do fim de pista, alinha os dois sensores
					motorDireita.run_forever(speed_sp=-150) #em branco
				else:
					motorDireita.run_forever(speed_sp=0)
				if(colors[SensorCorEsq.value()] != 'black'):
					motorEsquerda.run_forever(speed_sp=-150)
				else:
					motorEsquerda.run_forever(speed_sp=0)
			motorEsquerda.run_forever(speed_sp=0)
			motorDireita.run_forever(speed_sp=0)


def alinha():
	motorEsquerda.run_forever(speed_sp=0)
	motorDireita.run_forever(speed_sp=0)
	while(colors[SensorCorDir.value()] != 'white') or (colors[SensorCorEsq.value()] != 'white'):
		if(colors[SensorCorDir.value()] != 'white'): #Enquanto os dois não estiverem fora da interssecção ou fora do fim de pista, alinha os dois sensores
			motorDireita.run_forever(speed_sp=-150) #em branco
		else:
			motorDireita.run_forever(speed_sp=0)
		if(colors[SensorCorEsq.value()] != 'white'):
			motorEsquerda.run_forever(speed_sp=-150)
		else:
			motorEsquerda.run_forever(speed_sp=0)
	motorEsquerda.run_forever(speed_sp=0)
	motorDireita.run_forever(speed_sp=0)

def main(): #TESTES
	motorEsquerda.run_forever(speed_sp=200) #Começa o programa andando
	motorDireita.run_forever(speed_sp=200)
	#print("Sensor direito:", colors[SensorCorDir.value()])
	#print("Sensor esquerdo:", colors[SensorCorEsq.value()])
	if (colors[SensorCorDir.value()] != 'white') or (colors[SensorCorEsq.value()] != 'white'): #Condição de saída de pista
		if (colors[SensorCorDir.value()] == 'none') or (colors[SensorCorDir.value()] == 'black') or (colors[SensorCorEsq.value()] =='none') or (colors[SensorCorEsq.value()] == 'black'): #verificação Final da RUA
			sleep(0.2) #Esse IF verifica se está na borda ou no fim da rua. O SLEEP é pro robô andar um pouco pra ter certeza da condição
			if (colors[SensorCorDir.value()] == 'black') and (colors[SensorCorEsq.value()] =='black'): #Condição Fim de rua (Pós sleep)
				print("FIM DA RUA")
				alinha()
				motorEsquerda.run_forever(speed_sp=0)
				motorDireita.run_forever(speed_sp=0)
				sleep(0.3)
				girarRobo(180)
			elif (colors[SensorCorDir.value()] == 'none') or (colors[SensorCorDir.value()] == 'black') or (colors[SensorCorDir.value()] == 'brown') or (colors[SensorCorEsq.value()] =='none') or (colors[SensorCorEsq.value()] == 'black'):
				print("BORA PRA MANOBRA") #Condição de beirada da pista
				#manobra1()
				manobraextra()
		elif (colors[SensorCorDir.value()] == 'green') or (colors[SensorCorEsq.value()] =='green'): #pista subida
			sleep(0.2) #Sleep de garantia de condição
			if (colors[SensorCorDir.value()] == 'green') and (colors[SensorCorEsq.value()] =='green'):
				alinha() #Enquanto os dois não forem brancos ele fica alinhando!
				exit() #Estes exit são só a prévia para ver o funcionamento do programa. Sai do programa quando alinha de uma interssecção
		elif (colors[SensorCorDir.value()] == 'red') or (colors[SensorCorEsq.value()] =='red'): #pista descida
			sleep(0.2) #Sleep de garantia de condição
			if (colors[SensorCorDir.value()] == 'red') and (colors[SensorCorEsq.value()] =='red'):
				alinha()
				exit()

#--------------MAIN---------------------------------------------------------------------------------------------------------------------------------------------------------
while(True):
	main()
