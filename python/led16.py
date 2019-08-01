import RPi.GPIO as GPIO
import time

LED = 18

G1.setmode(GPIO.BCM)
G1.setup(LED, GPIO.OUT)

pwm = GPIO.PWM(LED, 100)

pwm.start(0)

try :
	while True :
		for value in range(0, 1024):
			pwm.changeDutyCycle(value / 10.23)
			time.sleep(0.005)

except :
	pwm.stop()
	GPIO.cleanup()
