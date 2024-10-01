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
