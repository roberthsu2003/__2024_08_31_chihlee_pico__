import machine
import time


adc = machine.ADC(4)
while True:
    temperature_value = adc.read_u16()
    print(temperature_value)
    time.sleep(3)

