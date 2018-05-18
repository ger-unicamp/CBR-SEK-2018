#pragma config(Sensor, S2,     gyro,           sensorEV3_Gyro)
//*!!Code automatically generated by 'ROBOTC' configuration wizard               !!*//

task main()
{
	int deg, head, rate;
	resetGyro(S2);
	while(){
		displayText(line1,"Degrees: ");
		/*
			getGyroDegrees
			Returns the accumulated value of the gyro sensor plugged into nDeviceIndex in degrees.
			Values returned will increment when the gyro is turning clockwise
			Values returned will decrement when the gyro is turning counter-clockwise
		*/
		deg = getGyroDegrees(S2);
		displayVariableValues(line2, deg);
		displayText(line3,"Heading: ");
		/*
			getGyroHeading
			Returns the heading of the gyro sensor plugged into nDeviceIndex based on the last "reset" point.
			This command is useful for making movements relative to the robot's last reset point, instead of its current position.
			Values returned will increment when the gyro is turning clockwise
			Values returned will decrement when the gyro is turning counter-clockwise
		*/
		head = getGyroHeading(S2);
		displayVariableValues(line4, head);
		displayText(line5,"Rate: ");
			/*
			getGyroRate
			Returns the current rate of movement for a gyro sensor
			Values are in degrees per second
			Values range from -440 to +440 degrees per second
		*/
		//rate = getGyroRate(S2);
		//displayVariableValues(line6, rate);
		wait(1);
	}
}
