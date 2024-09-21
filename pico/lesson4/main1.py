from machine import Pin
import time

led = Pin("LED", mode=Pin.OUT)
status = False
while True:
    if status == False:
        led.on()
        status = True
    else:
        led.off()
        status = False
    time.sleep(1)