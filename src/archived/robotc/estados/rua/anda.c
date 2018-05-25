#pragma config(Sensor, S1,     ult,            sensorEV3_Ultrasonic)
#pragma config(Sensor, S2,     cor,            sensorEV3_Color, modeEV3Color_Color)
#pragma config(Sensor, S3,     gyro,           sensorEV3_Gyro, modeEV3Gyro_RateAndAngle)
#pragma config(Motor,  motorA,          dir,           tmotorEV3_Large, PIDControl, encoder)
#pragma config(Motor,  motorB,          esq,           tmotorEV3_Large, PIDControl, encoder)
#pragma config(Motor,  motorC,          cancela,       tmotorEV3_Medium, PIDControl, encoder)

#define POTENCIA 80

/*Funcao andar reto
** Param: sentido
*/
void AndarReto (int sentido){
	setMotorSync(dir,esq,0,sentido*POTENCIA);
}

task main()
{
	while(true){
		AndarReto(1);
	}


}
