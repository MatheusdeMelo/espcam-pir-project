from machine import Pin
import camera

p0 = Pin(2, Pin.IN, Pin.PULL_UP)
file_path = "alert_image.jpg"
while True:
    if (p0.value() == 0):
        try:
            print("Taking a Photo!")
            camera.init(0, format=camera.JPEG)
            buffer = camera.capture()
            file = open(file_path, "w")
            file.write(buffer)
            file.close()
        except Exception as e:
            print("An issue ocurred!")
        finally:
            print("Deinitializing Camera")
            camera.deinit()
            break
