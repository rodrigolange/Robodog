#!/usr/bin/python


# Import required Python libraries
import time
import RPi.GPIO as GPIO

# Use BCM GPIO references
# instead of physical pin numbers
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

# Define GPIO to use on Pi
GPIO_TRIGGER = 23
GPIO_ECHO1   = 24
GPIO_ECHO2   = 25

# Set pins as output and input
GPIO.setup(GPIO_TRIGGER,GPIO.OUT)  # Trigger
GPIO.setup(GPIO_ECHO1,GPIO.IN)      # Echo
GPIO.setup(GPIO_ECHO2,GPIO.IN)      # Echo

# Set trigger to False (Low)
GPIO.output(GPIO_TRIGGER, False)

print("Ultrasonic Measurement")

# Allow module to settle
time.sleep(0.5)

# Send 10us pulse to trigger

while True:

	GPIO.output(GPIO_TRIGGER, True)
	time.sleep(0.00001)
	GPIO.output(GPIO_TRIGGER, False)
	start = 0
	stop = 0

	while GPIO.input(GPIO_ECHO1)==0:
		start = time.time()

	while GPIO.input(GPIO_ECHO1)==1:
		stop = time.time()

# Calculate pulse length
	elapsed = stop-start

# Distance pulse travelled in that time is time
# multiplied by the speed of sound (cm/s)
	distancet = elapsed * 34300

# That was the distance there and back so halve the value
	distance = distancet / 2

	print("Distance :", distance, " cm")
	#print("Elaspsed time :", elapsed)
	#print("Total distance :", distancet)


	time.sleep(1)
# Reset GPIO settings
GPIO.cleanup()
