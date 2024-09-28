from machine import Timer,ADC



adc = ADC(4)
conversion_factor = 3.3 / (65535)

def do_thing(t):
    reading = adc.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)



Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing)

