import ev3dev.ev3 as ev3
from time import sleep

# definicao de motores
motorDireita = LargeMotor('outA')
motorEsquerda = LargeMotor('outB')
motorGarra = MediumMotor('outC')

# definicao de sensores
ultrassonico = UltrasonicSensor() 
assert ultrassonico.connected, "Sensor ultrassonico nao conectado"
ultrassonico.mode = 'US-DIST-CM'

gyro = GyroSensor()
assert gyro.connected, "Giroscopio nao conectado"

sensorCor = ColorSensor()
assert sensorCor.connected, "Sensor de cor nao conectado"
sensorCor.mode(COL-COLOR)
colors=('unknown','black','blue','green','yellow','red','white','brown')
# print(colors[sensorCor.value()])

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
            motorDireita.run_forever(speed_sp=-100)
            motorEsquerda.run_forever(speed_sp=100)
            sleep(0.5)
            anguloSensor = gyro.value()

    else:
        while(anguloSensor > anguloDesejado + 4): # 4 eh para compensar o lag de leitura do gyro
            motorDireita.run_forever(speed_sp=100)
            motorEsquerda.run_forever(speed_sp=-100)
            sleep(0.5)
            anguloSensor = gyro.value()

    motorDireita.stop(stop_action="hold")
    motorEsquerda.stop(stop_action="hold")
    sleep(1)
    calibraGyro()
    
def agarrarBoneco():
    girarRobo(90)
    motorDireita.run_timed(time_sp=2000, speed_sp=200)
    motorEsquerda.run_timed(time_sp=2000, speed_sp=200)
    sleep(5)
    motorGarra.run_to_rel_pos(position_sp=220, speed_sp=100, stop_action="hold")
    sleep(5)
    motorDireita.run_timed(time_sp=2000, speed_sp=-200)
    motorEsquerda.run__timed(time_sp=2000, speed_sp=-200)
    sleep(5)
    girarRobo(-90)
    calibraGyro()

def main():	
    btn = Button()
    calibraGyro()	
    ev3.Sound.speak('Hello Humans!').wait()
    while btn.any()==False:
        distancia = ultrassonico.value()/10  # converte de mm para cm
        if(distancia < 20):
            motorDireita.run_forever(speed_sp=300)
            motorEsquerda.run_forever(speed_sp=300)
            sleep(0.5)
        else:
            motorDireita.stop(stop_action="hold")
            motorEsquerda.stop(stop_action="hold")
            sleep(2)
            agarrarBoneco()
    ev3.Sound.speak('Bye bye!').wait()

if __name__ == "__main__":
    main()
