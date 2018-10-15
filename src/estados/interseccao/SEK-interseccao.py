#!/usr/bin/env python3
# NOTE: SABER QUANDO O labyrinth ESTARA PRONTO -> RAMPA
#NOTE: TRATAR A COR DE AMBOS OS LADOS? TO USANDO SÓ UM LADO PRA verificacao
#NOTE: VER CONDICAO DE COR PARA NAO CONFUNDIR COM O AJUSTE DE LINEARIDADE(RUA)

from ev3dev.ev3 import *
from time import sleep

class Interseccao:
    def __init__(self):
        self.inter = {'2': -1, '3': -1, '5': -1}#as chaves sao as cores, comeca com -1 pq ainda n sabemosa  direcao
        self.verify_dir = -1#variavel para verificacao da direcao a ser 'pushed'
    def push(self, cor, direcao):
        if(direcao==0):
            self.inter['{}'.format(cor)]=self.verify_dir
        else:
            self.inter['{}'.format(cor)] = direcao
        self.verify_dir =-1
    def acessa(self, cor):
        return self.inter['{}'.format(cor)]
	def where_to_go(self, cor):
		if self.iter['{}'.format(cor)] != -1:
			return self.iter['{}'.format(cor)]
		else:
			if 0 not in self.inter.values():
                self.verify_dir+=1
                return 0
			elif 1 not in self.inter.values() and self.verify_dir==-1:
                self.verify_dir+=1
                return 1
			# elif 2 not in self.inter.values():
            #     return 2
            else:
                self.verify_dir = 2
                return 0
    def __str__(self):
        return '{}'.format(self.inter)


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

# Variaveis Globais
path = list() #lista com as direcoes a serem seguidas pelo trajeto (path)
labyrinth = False
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

def main():
    btn = Button()
	interseccao = Interseccao()
    calibraGyro()
	push = False #variavel para salvar as infos na interseccao
	cor = 0 #none
	direcao = 0 #cuidados com escopo de condicional
    Sound.speak('Hello Humans!').wait()
    motorDireita.run_forever(speed_sp=200)
    motorEsquerda.run_forever(speed_sp=200)
    while not btn.any():
        if sensorCorDir.value() != 6 and sensorCorEsq.value() != 6:
            if sensorCorDir.value() != 1 and sensorCorEsq.value() != 1:
				push = True
				old_color = cor
				motorDireita.run_timed(time_sp=1600, speed_sp=200)
                motorEsquerda.run_timed(time_sp=1600, speed_sp=200)
				cor = sensorCorDir.value()
				sleep(2)
				if not labyrinth:
					if push and (old_color==2 or old_color==3 or old_color==5):
						interseccao.push(old_color, direcao)
					direcao = interseccao.where_to_go(sensorCorDir.value())
					if direcao == 0:
						girarRobo(90)
						motorDireita.run_forever(speed_sp=200)
		                motorEsquerda.run_forever(speed_sp=200)
		                sleep(4)
					elif direcao == 1:
						motorDireita.run_forever(speed_sp=200)
		                motorEsquerda.run_forever(speed_sp=200)
		                sleep(4)
					elif direcao == 2:
						girarRobo(-90)
						motorDireita.run_forever(speed_sp=200)
		                motorEsquerda.run_forever(speed_sp=200)
		                sleep(4)
				if labyrinth:
					direcao = interseccao.acessa(sensorCorDir.value())
					if direcao == 0:
						girarRobo(90)
						motorDireita.run_forever(speed_sp=200)
		                motorEsquerda.run_forever(speed_sp=200)
		                sleep(4)
					elif direcao == 1:
						motorDireita.run_forever(speed_sp=200)
		                motorEsquerda.run_forever(speed_sp=200)
		                sleep(4)
					elif direcao == 2:
						girarRobo(-90)
						motorDireita.run_forever(speed_sp=200)
		                motorEsquerda.run_forever(speed_sp=200)
		                sleep(4)
            elif sensorCorDir.value()==1 and sensorCorEsq.value()==1:
				push = False
                cor = 0
                motorDireita.run_timed(time_sp=1400, speed_sp=-200)
                motorEsquerda.run_timed(time_sp=1400, speed_sp=-200)
                girarRobo(90)
				girarRobo(90)
                motorDireita.run_forever(speed_sp=200)
                motorEsquerda.run_forever(speed_sp=200)
if __name__=="__main__":
    main()
