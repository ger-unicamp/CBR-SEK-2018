/*
Função para usar no robô do SEK - 2017
Uso de sensor de cor. É importante que o sensor seja configurado com o modo "cor".
author: Tiago

Color name (TLegoColors)                                           		Enumerated Value
colorNone:      No object is detected by the color sensor                   0
colorBlack:     A black object is detected by the color sensor              1
colorBlue:      A blue object is detected by the color sensor               2
colorGreen:     A green object is detected by the color sensor              3
colorYellow:    A yellow object is detected by the color sensor             4
colorRed:       A red object is detected by the color sensor                5
colorWhite:     A white object is detected by the color sensor              6
colorBrown:     A brown object is detected by the color sensor              7
*/

/* 	Função get color que pode ser chamada no código principal ou em outras funções
		Evita quando o sensor não encontra nenhum objeto
		Retorna cor do tipo TLegoColors
		Parâmetro é a porta do sensor: S1, S2, S3, S4
*/
TLegoColors getColor(tSensors sensor){
	bool getColor = false;
	TLegoColors color;

	while(!getColor){
		color = getColorName(sensor);
		if(color != colorNone)
			getColor = true;
		else
			getColor = false;
	}

	return color;
}

string colorName;

// o main abaixo pode ser modificado, foi usado apenas para testar o sensor
task main()
{
	while(true){
	switch(getColor(S2)){
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
				// muitas vezes a leitura é rápida e o ev3 não identifica a cor lida, retornando "none"
				colorName = "none";
				break;
		}
		displaySensorValues(8,S2);
	  displayText(9,colorName);
	  writeDebugStreamLine("Colour detected: %s", colorName);
	  sleep(1000);
	}
}
