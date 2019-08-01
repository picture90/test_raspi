import RPi.GPIO as GPIO
import time 

R1 = 17
G1 = 18
B1 = 27

R2 = 22
G2 = 23
B2 = 24

R3 = 5
G3 = 6
B3 = 13

GPIO.setmode(GPIO.BCM)
GPIO.setup(R1, GPIO.OUT)
GPIO.setup(G1, GPIO.OUT)
GPIO.setup(B1, GPIO.OUT)

GPIO.setup(R2, GPIO.OUT)
GPIO.setup(G2, GPIO.OUT)
GPIO.setup(B2, GPIO.OUT)

GPIO.setup(R3, GPIO.OUT)
GPIO.setup(G3, GPIO.OUT)
GPIO.setup(B3, GPIO.OUT)

pwm = [
    [GPIO.PWM(R1, 120), GPIO.PWM(G1, 120), GPIO.PWM(B1, 120)],
    [GPIO.PWM(R2, 120), GPIO.PWM(G2, 120), GPIO.PWM(B2, 120)],
    [GPIO.PWM(R3, 120), GPIO.PWM(G3, 120), GPIO.PWM(B3, 120)]
]

for i in range(0, len(pwm)) :
    for j in range(0, len(pwm[i])):
        pwm[i][j].start(0)
def Ledcolorset1(r, g, b) :
    pwm[0][0].ChangeDutyCycle(r / 2.55)
    pwm[0][1].ChangeDutyCycle(g / 2.55)
    pwm[0][2].ChangeDutyCycle(b / 2.55)

def Ledcolorset2(r, g, b) :
    pwm[1][0].ChangeDutyCycle(r / 2.55)
    pwm[1][1].ChangeDutyCycle(g / 2.55)
    pwm[1][2].ChangeDutyCycle(b / 2.55)

def Ledcolorset3(r, g, b) :[
    pwm[2][0].ChangeDutyCycle(r / 2.55)
    pwm[2][1].ChangeDutyCycle(g / 2.55)
    pwm[2][2].ChangeDutyCycle(b / 2.55)
]
freq = [
    [[0, 1], [100, 1], [200, -1]],
    [[200, -1], [100, 1], [0, 1]],
    [[100, 1], [200, -1], [0,1]]
]

try :
    print("Ctrl + C¸¦ ´­·¯ Á¾·áÇÕ´Ï´Ù.")
    while True :

        for i in range(0, len(freq)) :
            for j in range(0, len(freq[i])) :
                freq[i][j][0] += freq[i][j][1]
                if freq[i][j][0] >= 256:
                  freq[i][j][0] = 255
                  freq[i][j][1] = -1
                elif freq[i][j][0] <= -1 :
                    freq[i][j][0] = 0
                    freq[i][j][0] = 1

        Ledcolorset1(freq[0][0][0], freq[0][1][0], fleq[0][2][0])
        Ledcolorset1(freq[1][0][0], freq[1][1][0], fleq[1][2][0])
        Ledcolorset1(freq[2][0][0], freq[2][1][0], fleq[2][2][0])
        time.sleep(0.005)

except :

        for i in range(0, len(pwm)) :
             for j in range(0, len(pwm[i])) :
                 pwm[i][j].stop()
        GPIO.cleanup()
        print("end")
