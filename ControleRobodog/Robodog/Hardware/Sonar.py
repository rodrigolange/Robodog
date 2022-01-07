import time
import RPi.GPIO as GPIO

class Sonar:

	def __init__(self, trigger, echo):

		# Use BCM GPIO references instead of physical pin numbers
		GPIO.setmode(GPIO.BCM)
		GPIO.setwarnings(False)
		self.GPIO_TRIGGER = trigger # sonar esquerda
		self.GPIO_ECHO    = echo # sonar esquerda

		# Set pins as output and input
		GPIO.setup(self.GPIO_TRIGGER,GPIO.OUT)  # Trigger
		GPIO.setup(self.GPIO_ECHO,GPIO.IN)      # Echo

		# Set trigger to False (Low)
		GPIO.output(self.GPIO_TRIGGER, False)
		# Allow module to settle
		time.sleep(0.5)

	def getDistancia(self):
		start = 0
		stop = 0

		GPIO.output(self.GPIO_TRIGGER, True)
		time.sleep(0.00001)
		GPIO.output(self.GPIO_TRIGGER, False)

		while GPIO.input(self.GPIO_ECHO)==0:
			start = time.time()

		while GPIO.input(self.GPIO_ECHO)==1:
			stop = time.time()

		# Calculate pulse length
		elapsed = stop-start

		# Distance pulse travelled in that time is time
		# multiplied by the speed of sound (cm/s)
		distance = (elapsed * 34300)/2
		return distance
