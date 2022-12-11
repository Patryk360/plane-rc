from time import sleep
from machine import Pin, PWM

servoLeft = PWM(Pin(7))
servoLeft.freq(50)

servoMin=2000
servoMax=8550

def servo(degrees):
    for degree in range(0, degrees+1, 1):
        duty=servoMin+(servoMax-servoMin)*(degree/180)
        servoLeft.duty_u16(int(duty))
        sleep(0.001)

RPWM=Pin(16, Pin.OUT)
EN_PWM_R=PWM(Pin(17))
EN_PWM_R.freq(10000)

LPWM=Pin(15, Pin.OUT)
EN_PWM_L=PWM(Pin(14))
EN_PWM_L.freq(10000)


while True:
    RPWM.high()

    sleep(1)

    for duty in range(30000, 65025, 1):
        EN_PWM_R.duty_u16(duty)
        sleep(0.0001)

    sleep(8)

    for duty in range(65025, 30000, -1):
        EN_PWM_R.duty_u16(duty)
        sleep(0.0001)

    sleep(1)

    RPWM.low()

    sleep(1)

    LPWM.high()

    sleep(1)

    for duty in range(30000, 65025, 1):
        EN_PWM_L.duty_u16(duty)
        sleep(0.0001)

    sleep(8)

    for duty in range(65025, 30000, -1):
        EN_PWM_L.duty_u16(duty)
        sleep(0.0001)

    sleep(1)

    LPWM.low()

    sleep(1)

    servo(0)

    sleep(1)

    servo(180)

    sleep(1)

    servo(90)

    sleep(1)

    servo(45)

    sleep(1)

    servo(135)

    sleep(1)