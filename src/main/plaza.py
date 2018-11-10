'''
GER PLAZA 06/11/2018

Codigo usado para competicao CBR-SEK-2018 no estado plaza
ALGORITMO.:
passar pela rampa_ida:
alinhar vermelho com o branco - e ficar no vermelho
alinhar verde com o branco - e ficar no branco

passar pela rampa_volta:
alinhar verde com o branco - e ficar no verde
alinhar vermlho com o branco - e ficar no vermelho

depositar boneco:
seguir reto de acordo com a distancia dada pela ultrassonico e sensor de cor
abrir garra;
fechar garra (?)

voltar para rua - girar no proprio eixo - sentido == -1 (andar de re) ; sentido == 1 (andar frente)
girar para direita e seguir de re
girar para esquerda e seguir de re
girar direita, andar um pouco para tras
seguir reto até o sensor ultrassonico retornar x
girar para esquerda
desce a rampa

'''
from ev3dev.ev3 import *
from time import sleep

#variaveis globais e flags------------------------------------------------------
colors=('none','black','blue','green','yellow','red','white','brown')
distMax = 84 #distancia maxima da parede para se manter centralizado
distMin = 76 #distancia minima para se manter centralizado
primeiroRe = 8 #sleep para percorrer o plaza (largura)
segundoRe = 8 #sleep para percorrer o plaza (comprimento)
distSaida = 40 #valor do ultrassonico para sair do plaza
plazaSentido = 0 #flag para muadr o sentido do plaza - 0 chegada; 1 saida
gyro_const = 4
 

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

#funcoes dos sensores e dos subestados -------------------------------------------------------------
def ultra():
    aux = [ultrassonico.value()/10 for i in range(10)]
    aux.sort()
    return aux[4]

def calibraGyro():
    gyro.mode = 'GYRO-RATE'
    sleep(0.3)
    gyro.mode = 'GYRO-ANG'
    sleep(0.3)

def alinha(sentido):
    print('ALINHA')
    motorEsquerda.stop(stop_action = 'hold')
    motorDireita.stop(stop_action = 'hold')
    while(colors[SensorCorDir.value()] != 'white') or (colors[SensorCorEsq.value()] != 'white'):
        if(colors[SensorCorDir.value()] != 'white'): #Enquanto os dois não estiverem fora da interssecção ou fora do fim de pista, alinha os dois sensores
            motorDireita.run_forever(speed_sp=-180*sentido) #em branco
        else:
            motorDireita.stop(stop_action = 'hold')
        if(colors[SensorCorEsq.value()] != 'white'):
            motorEsquerda.run_forever(speed_sp=-180*sentido)
        else:
            motorEsquerda.stop(stop_action = 'hold')
    motorEsquerda.stop(stop_action = 'hold')
    motorDireita.stop(stop_action = 'hold')

def girarRobo(anguloDesejado):
    calibraGyro()
    anguloSensor = gyro.value()
    if(anguloDesejado > 0):
        while(anguloSensor < anguloDesejado - gyro_const): # 4 eh para compensar o lag de leitura do gyro
            motorDireita.run_forever(speed_sp=0)
            motorEsquerda.run_forever(speed_sp=150)
            anguloSensor = gyro.value()
    else:
        while(anguloSensor > anguloDesejado + gyro_const): # 4 eh para compensar o lag de leitura do gyro
            motorDireita.run_forever(speed_sp=150)
            motorEsquerda.run_forever(speed_sp=0)
            anguloSensor = gyro.value()

    motorDireita.stop(stop_action="hold")
    motorEsquerda.stop(stop_action="hold")
    calibraGyro()

def andar(timeSleep, sentido):
    motorDireita.run_forever(speed_sp=200*sentido)
    motorEsquerda.run_forever(speed_sp=200*sentido)
    sleep(timeSleep)

'''
def alinhaRampa():
    global plazaSentido

    motorEsquerda.run_forever(speed_sp=0)
    motorDireita.run_forever(speed_sp=0)
    while(colors[SensorCorDir.value()] != colors[SensorCorEsq.value()]): # se os sensores for diferentes
        if(colors[SensorCorDir.value()] == 'red'): # se o esquerdo for branco
            if(plazaSentido == 1):
                motorEsquerdo.run_forever(speed_sp=100) # alinhar no vermelho se o for sentido chegada
            else:
                motorDireita.run_forever(speed_sp=-100) # alinhar no branco se o for sentido saida
        if(colors[SensorCorDir.value()] == 'green'):
             if(plazaSentido == 1):
                motorEsquerdo.run_forever(speed_sp=100) # alinhar no vermelho se o for sentido chegada
            else:
                motorDireita.run_forever(speed_sp=-100) # alinhar no branco se o for sentido saida

        if(colors[SensorCorDir.value()] == 'green')
        else:
            motorDireita.run_forever(speed_sp=0)
       
        if(colors[SensorCorEsq.value()] != 'white'):
            motorEsquerda.run_forever(speed_sp=-100)
        else:
            motorEsquerda.run_forever(speed_sp=0)
    motorEsquerda.run_forever(speed_sp=0)
    motorDireita.run_forever(speed_sp=0)
'''

def depositarBoneco():
    print('comecei depositarBoneco')
    global plazaSentido
    global distMin
    global distMax

    while((colors[SensorCorDir.value()] != "black") and (colors[SensorCorDir.value()] != "none")) or ((colors[SensorCorEsq.value()] != "none") and (colors[SensorCorEsq.value()] != "black")): # se manter no centro do plaza
        motorDireita.run_forever(speed_sp=200)
        motorEsquerda.run_forever(speed_sp=200)
        print('sensor direito ' + str(colors[SensorCorDir.value()]))
        print('sensor esquerdo ' + str(colors[SensorCorEsq.value()]))
        dist = ultra()
        print('dist: ' + str(dist))
        if(dist < distMin): # arrumar para direita
            print('arrumar para direita')
            motorDireita.run_forever(speed_sp=200)
            motorEsquerda.run_forever(speed_sp=180)
        if(dist > distMax): # arrumar para esquerda
            print('arrumar para esquerdo')
            motorDireita.run_forever(speed_sp=180)
            motorEsquerda.run_forever(speed_sp=200)
    sleep(0.1)
    motorDireita.stop(stop_action = 'hold')
    motorEsquerda.stop(stop_action = 'hold')
    if(colors[SensorCorDir.value()] == "black") and (colors[SensorCorEsq.value()] == "black"):
        sleep(0.1) #Esse sleep serve para não ficar na borda do centro preto
        motorDireita.stop(stop_action = 'hold')
        motorEsquerda.stop(stop_action = 'hold')
        motorGarra.run_to_rel_pos(position_sp=290, speed_sp=100, stop_action="hold") #abre H ra
    sleep(1.7)
    motorDireita.run_forever(speed_sp=-200)
    motorEsquerda.run_forever(speed_sp=-200)
    sleep(0.8)
    plazaSentido = 1

def voltaRua():
    global primeiroRe
    global segundoRe
    global distSaida
    global plazaSentido 
    dist = ultra()

    girarRobo(90)
    andar(primeiroRe,-1)
    girarRobo(-90)
    andar(segundoRe,-1)
    girarRobo(90)
    andar(1.5,-1) # encontar na parede e ficar reto

    # procurar a 
    dist = ultra()
    while(dist < distSaida):
        print('ultra ' + str(ultra()))
        motorDireita.run_forever(speed_sp=150)
        motorEsquerda.run_forever(speed_sp=150)
        dist = ultra()

    motorDireita.stop(stop_action = 'hold')
    motorEsquerda.stop(stop_action = 'hold')
    print('vi a saida e dist: ' + str(dist))
    andar(0.04,1) # se centralizar na porta de saida
    girarRobo(90)
    plazaSentido = 0


def plaza():
    '''
    while(colors[SensorCorDir.value()] == 'white' or colors[SensorCorEsq.value()] == 'white'):
        motorEsquerda.run_forever(speed_sp=100)
        motorDireita.run_forever(speed_sp=100)
    motorDireita.stop(stop_action = 'hold')
    motorEsquerda.stop(stop_action = 'hold')
    
    motorEsquerda.run_forever(speed_sp=-150)
    motorDireita.run_forever(speed_sp=-150)
    sleep(2)
    #motorDireita.run_timed(time_sp = 3000, speed_sp =-170)
    #motorEsquerda.run_timed(time_sp = 3000, speed_sp =-170)
    motorDireita.stop(stop_action = 'hold')
    motorEsquerda.stop(stop_action = 'hold')
    while(colors[SensorCorDir.value()] == 'white' and colors[SensorCorEsq.value()] == 'white'):
        motorEsquerda.run_forever(speed_sp=150)
        motorDireita.run_forever(speed_sp=150)
    motorDireita.stop(stop_action = 'hold')
    motorEsquerda.stop(stop_action = 'hold')
    if(colors[SensorCorDir.value()] == 'red'):
        while(colors[SensorCorDir.value()] == 'red'):
            motorDireita.run_forever(speed_sp = -150)
        motorDireita.stop(stop_action = 'hold')
    if(colors[SensorCorEsq.value()] == 'red'):
        while(colors[SensorCorEsq.value()] == 'red'):
            motorEsquerda.run_forever(speed_sp = -150)
        motorEsquerda.stop(stop_action = 'hold')
    
    motorDireita.stop(stop_action = 'hold')
    motorEsquerda.stop(stop_action = 'hold')
    
    alinha(1)
    motorEsquerda.run_forever(speed_sp=150)
    motorDireita.run_forever(speed_sp=150)
    sleep(4) #testar 
    '''
    print('comecou')
    depositarBoneco()
    print('deixou boneco')
    sleep(0.2)
    print('volta rua')
    voltaRua()

'''
if __name__== '__main__':
    Sound.speak('Hello Humans!').wait()
    plaza()
'''




