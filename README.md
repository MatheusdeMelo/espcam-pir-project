# ESPCAM-PIR PROJECT
Project with EspCam (using MicroPython), PIR sensor and servo for represents a residential security system to protect property invasions.

## Directories Organization
```bash
firmwares/ #store EspCam firmwares
.tool-versions #store languages (Python) versions
alert_image.jpg #example image
boot.py #file with code that runs in all boots
cam.py #file with test camera code
net.py #file with main code
servo-motor.py #file with test servo code
umail.py #file that config umail library
```

## Main Code
The main code is stored in file **net.py** and can be splited in 3 fields: configuration, definition and application.

### 1- Configuration field
```bash
import time
import network
import umail
import ubinascii
from machine import Pin,PWM
import camera

ssid = "ssid"
wf_pass = "wifi_password"

sender_email = 'your@gmail'
sender_name = 'YOUR_NAME' #sender name
sender_app_password = 'app_password'
recipient_email = ['1@gmail.com', '2@gmail.com']
email_subject ='EspCam Alert'

text = "Olá! \nUm intruso foi capturado pelo EspCam.\nO próximo email consta com a foto do intruso!"
p0 = Pin(2, Pin.IN, Pin.PULL_DOWN)
p1 = Pin(14, Pin.OUT)
servo = PWM(Pin(15, mode=Pin.OUT))
```
With the **import** command the libraries are required, in this project you'll use time, network, umail, ubinascii, machine and camera libraries.
"ssid" and "wf_pass" are the variables for wifi connection configuration and after then email configuration variables are configured.

"text" variable stores the text that will be sended in text email, "p0" and "p1" defines pins of in and out, respectively, and "servo" variable defines PWM out pin.
