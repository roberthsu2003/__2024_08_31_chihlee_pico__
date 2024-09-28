from machine import Timer,ADC,Pin



adc = ADC(4)
conversion_factor = 3.3 / (65535)

def do_thing(t):
    reading = adc.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    
def do_thing1(t):
    adc1 = ADC(Pin(26))
    duty = adc1.read_u16()
    
    print(f'可變電阻:{round(duty/65535*10)}')



t1 = Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing)
t2 = Timer(period=500, mode=Timer.PERIODIC, callback=do_thing1)

