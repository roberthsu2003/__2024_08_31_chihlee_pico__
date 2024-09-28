from machine import Timer,ADC



adc = ADC(4)
conversion_factor = 3.3 / (65535)

def do_thing(t):
    reading = adc.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    print(temperature)
    
def do_thing1(t):
    print("do_thing1")



t1 = Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing)
t2 = Timer(period=500, mode=Timer.PERIODIC, callback=do_thing1)

