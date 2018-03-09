/*
		Teste da função getColorName. Essa função retorna a cor segundo o código de cores abaixo:

		Color name                                                          Enumerated Value
		colorNone:      No object is detected by the color sensor                   0
		colorBlack:     A black object is detected by the color sensor              1
		colorBlue:      A blue object is detected by the color sensor               2
		colorGreen:     A green object is detected by the color sensor              3
		colorYellow:    A yellow object is detected by the color sensor             4
		colorRed:       A red object is detected by the color sensor                5
		colorWhite:     A white object is detected by the color sensor              6
		colorBrown:     A brown object is detected by the color sensor              7

		Uso para testes. O programa printa na tela do EV3 a cor identificada.
		É importante que o sensor seja configurado com o modo "cor".
*/
string colorName;

task main()
{
	while(true){
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
