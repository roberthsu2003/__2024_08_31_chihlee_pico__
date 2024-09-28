from machine import Timer,ADC,Pin,PWM,RTC



adc = ADC(4)
pwm = PWM(Pin(15),freq=50)
conversion_factor = 3.3 / (65535)
rtc = RTC()

def do_thing(t):
    reading = adc.read_u16() * conversion_factor
    temperature = 27 - (reading - 0.706)/0.001721
    year,month,day,weekly,hours,minuse,seconds,info = rtc.datetime()
    datetime_str = f"{year}-{month}-{day} {hours}:{minuse}:{seconds}"
    print(datetime_str)
    print(temperature)
    
def do_thing1(t):
    adc1 = ADC(Pin(26))
    duty = adc1.read_u16()
    pwm.duty_u16(duty)
    
    print(f'可變電阻:{round(duty/65535*10)}')



t1 = Timer(period=2000, mode=Timer.PERIODIC, callback=do_thing)
t2 = Timer(period=500, mode=Timer.PERIODIC, callback=do_thing1)

