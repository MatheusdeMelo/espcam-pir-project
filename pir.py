from machine import Pin,PWM
import camera
from time import sleep

#sg90 = PWM(Pin(15, mode=Pin.OUT))
#sg90.freq(50)
p0 = Pin(2, Pin.IN, Pin.PULL_DOWN)
counter = 0

while True:
    if p0.value() == 0:
        counter += 1
        print("Nautico:", counter)
    print("Vasco")