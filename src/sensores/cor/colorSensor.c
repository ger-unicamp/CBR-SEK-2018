/* Função para Retornar a Cor lida pelo Sensor
** Params: porta conectada do sensor de cor
** Retorna: cor lida pelo sensor
** Ref: http://help.robotc.net/WebHelpMindstorms/index.htm#Resources/topics/LEGO_EV3/ROBOTC/Sensors/Color_Sensor/Color-Sensor.htm
**
** Essa funcao deve ter seus parametros alterados por calibracao.	
**
*/
TLegoColors getColor(tSensors sensor){
	long int redValue;
	long int greenValue;
	long int blueValue;

	// Pega os valores de verde, vermelho e azul e grava nas respectivas variaveis
	getColorRGB(sensor, redValue, greenValue, blueValue);
	// valores rgb são calibrados para que o metodo funcione corretamente
	// se alguma COR for detectada
	if((redValue >= 5) || (greenValue >= 5) || (blueValue >= 5)){
		// BRANCO
		if(redValue >= 60 && greenValue >= 60 && blueValue >= 35){
			return colorWhite;
			}else{
			// VERDE
			if((redValue <= 12) && (greenValue >= 15) && (blueValue <= 13)){
				return colorGreen;
				}else{
				// VERMELHO MALDITO
				if((redValue >= 40) && (greenValue <= 10) && (blueValue <= 10)){
					return colorRed;
					}else{
					// AMARELO
					if((redValue >= 50) && (greenValue >= 20) && (blueValue <= 10)){
						return colorYellow;
						}else{
						// AZUL
						if((redValue <= 15) && (greenValue >= 25) && (blueValue >= 25)){
							return colorBlue;
							}else{

							// PRETO
							if((redValue <= 10) && (greenValue <= 10) && (blueValue <= 10)){
								return colorBlack;
							}
						}
					}
				}
			}
		}
	}
	// nenhuma cor lida
	return colorNone;
}

/*
** Teste da funçăo getColorName. Essa funçăo retorna a cor segundo o código de cores abaixo:
** Params: porta conectada do sensor de cor
** Retorna: void
** Ref: http://help.robotc.net/WebHelpMindstorms/index.htm#Resources/topics/LEGO_EV3/ROBOTC/Sensors/Color_Sensor/getColorName.htm
** 
** Color name                                                          Enumerated Value
** colorNone:      No object is detected by the color sensor                   0
** colorBlack:     A black object is detected by the color sensor              1
** colorBlue:      A blue object is detected by the color sensor               2
** colorGreen:     A green object is detected by the color sensor              3
** colorYellow:    A yellow object is detected by the color sensor             4
** colorRed:       A red object is detected by the color sensor                5
** colorWhite:     A white object is detected by the color sensor              6
** colorBrown:     A brown object is detected by the color sensor              7
** Uso para testes. O programa printa na tela do EV3 a cor identificada.
**	
** Eh importante que o sensor seja configurado com o modo "cor".
** Essa funcao se tornou menos eficiente do que ler valores RGB individualmente.
**
*/
void getColorNameTest(){
	string colorName;
	switch(getColorName(S2)){
			case colorBlack:
				colorName = "black";
				break;
			case colorBlue:
				colorName = "blue";
				break;
			case colorRed:
				colorName = "red";
				break;
			case colorGreen:
				colorName = "green";
				break;
			case colorBrown:
				colorName = "brown";
				break;
			case colorWhite:
				colorName = "white";
				break;
			case colorYellow:
				colorName = "yellow";
				break;
			default:
				// muitas vezes a leitura eh muito rapida e o ev3 nao identifica a cor lida, retornando "none"
				colorName = "none";
				break;
	}
	displaySensorValues(8,S2);
	displayText(9,colorName);
	writeDebugStreamLine("Colour detected: %s", colorName);
	sleep(1000);
}

task main()
{
	while(true){}	
}