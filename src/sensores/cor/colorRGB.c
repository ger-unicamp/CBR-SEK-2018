long redValue;
long greenValue;
long blueValue;

task main()
{
	//Infinite Loop
	while (true)
	{
		//Get the value of all three channels of the color sensor
		//and store it in the variables
		getColorRGB(S2, redValue, greenValue, blueValue);

		//Write the values to the Debug Stream
	  writeDebugStreamLine("Colour detected: %d, %d, %d", redValue, greenValue, blueValue);
		sleep(100);
	}
}
