# ESPCAM-PIR PROJECT
Project with EspCam (using MicroPython), PIR sensor and servo for represents a residential security system to protect property invasions.

## Directories Organization
```bash
firmwares/      #store EspCam firmwares
.tool-versions  #store languages (Python) versions
alert_image.jpg #example image
boot.py         #file with code that runs in all boots
cam.py          #file with test camera code
net.py          #file with main code
servo-motor.py  #file with test servo code
umail.py        #file that config umail library
```

## The Main Code
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

### 2- Definition field
```bash
def connect_wifi(ssid, password):
  #Connect to your network
  station = network.WLAN(network.STA_IF)
  station.active(True)
  station.connect(ssid, password)
  while station.isconnected() == False:
    pass
  print('Connection successful')
  print(station.ifconfig())

def send_photo_email():
    smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True) # Gmail's SSL port
    smtp.login(sender_email, sender_app_password)
    smtp.to(recipient_email)
    smtp.write("From:" + sender_name + "<"+ sender_email+">\n")
    smtp.write("Subject:" + email_subject + "\n")
    smtp.write("Content-Type: image/jpeg;\n name=captured_image.jpg\nContent-Transfer-Encoding: base64\nContent-Disposition: attachment;\n  filename=captured_image.jpg\r\n")
    camera.init(0, format=camera.JPEG)
    buffer = camera.capture()
    b64 = ubinascii.b2a_base64(buffer)
    camera.deinit()
    smtp.write(b64)
    smtp.send()
    smtp.quit()

def send_text_email(text):
    smtp = umail.SMTP('smtp.gmail.com', 465, ssl=True) # Gmail's SSL port
    smtp.login(sender_email, sender_app_password)
    smtp.to(recipient_email)
    smtp.write("From:" + sender_name + "<"+ sender_email+">\n")
    smtp.write("Subject:" + email_subject + "\n")
    smtp.write(text)
    smtp.send()
    smtp.quit()
```

In this field, multiple important functions are defined. The first function configures the Wi-Fi connection; it uses the network library and requires two parameters: SSID and password. The second and third functions are similar because they both serve the same purpose: sending emails using SMTP. However, the second function sends an email with a photo captured by EspCam, while the third sends an email with an alert message.

### 3- Application field
```bash
connect_wifi(ssid, wf_pass)
servo.freq(50)
while True:
    if(p0.value() == 1):
        print("Pegamos!")
        p1.value(1)
        send_text_email(text)
        send_photo_email()
        p1.value(0)
        print("Trancando a porta!")
        for i in range(80):
            servo.duty(40+i)
            time.sleep(0.1)
        time.sleep(2)
        print("Ameaça contida. Destrancando a porta!")
        for i in range(80):
            servo.duty(120-i)
            time.sleep(0.17)
```

The last code section applies what was configured in other parts of the code. It initializes the Wi-Fi connection and the servo frequency. After that, a while loop waits for a signal from the PIR sensor pin. If motion is detected, it follows these steps: prints a message, turns on the LED, sends the text and photo emails, turns off the LED, "closes the door" by moving the servo, and opens it again after 2 seconds.  
