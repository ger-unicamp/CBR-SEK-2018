//Creates variables to store the red, green, and blue values
long redValue;
long greenValue;
long blueValue;

    //Infinite Loop
    while (true)
    {
    //Get the value of all three channels of the color sensor
    //and store it in the variables
    getColorRGB(colorSensor, redValue, greenValue, blueValue);

    //Write the values to the Debug Stream
    // http://help.robotc.net/WebHelpMindstorms/index.htm#Resources/topics/ROBOTC_Debugger/Debug_Windows/Debug_Stream.htm
      writeDebugStreamLine("Colour detected: %d, %d, %d", redValue, greenValue, blueValue);
        sleep(100);
    