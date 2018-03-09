//This program will continually check the color sensor
//and store the name of the color detected by it in the
//colorOfObject string

/*
Color name                                                          Enumerated Value
colorNone:      No object is detected by the color sensor                   0
colorBlack:     A black object is detected by the color sensor              1
colorBlue:      A blue object is detected by the color sensor               2
colorGreen:     A green object is detected by the color sensor              3
colorYellow:    A yellow object is detected by the color sensor             4
colorRed:       A red object is detected by the color sensor                5
colorWhite:     A white object is detected by the color sensor              6
colorBrown:     A brown object is detected by the color sensor              7
*/
 
//String used to store the color of the object
string colorOfObject;
 
//Keep looping forever
repeat(forever)
{
    //If the color sensor plugged into port 3 returns
    // the colorRed name (a red object is detected)
    if(getColorName(S3) == colorRed)
    {
        //Store the text RED into the color string
        colorOfObject = "RED";
    }
     
    //If the color sensor plugged into port 3 returns
    // the colorBlue name (a Blue object is detected)
    else if(getColorName(S3) == colorBlue)
    {
        //Store the text Blue into the color string
        colorOfObject = "BLUE";
    }
}