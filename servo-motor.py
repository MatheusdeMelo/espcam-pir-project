from machine import Pin,PWM
import time

sg90 = PWM(Pin(15, mode=Pin.OUT))
led = PWM(Pin(14, Pin.OUT))
sg90.freq(50)
#counter = 80 # metade do caminho
counter = 50 # caminho total
p0 = Pin(02, Pin.IN, Pin.PULL_DOWN)
# 0.5ms/20ms = 0.025 = 2.5% duty cycle
# 2.4ms/20ms = 0.12 = 12% duty cycle

# 0.025*1024=25.6
# 0.12*1024=122.88

while True:
    #led.duty(128)
    #led.freq(1)
    for i in range(80):
        sg90.duty(40+i)
        time.sleep(0.1)
        print("Growing:", 40+i)
    for i in range(80):
        sg90.duty(120-i)
        time.sleep(0.17)
        print("Decreasing:", 120-i)
    #sg90.duty(123)
    #time.sleep(15)
    #led.value(0)