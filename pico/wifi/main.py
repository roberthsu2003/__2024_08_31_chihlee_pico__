from tools import connect,reconnect
import urequests as requests
import utime
from machine import Timer
   
def callback1(t:Timer):
        
    url = 'xxxxx'    
    
    try:
	     #如果server 沒有回應,不會有response     
        response = requests.get(url)        
    except:
        reconnect()
    else:
        print("server接收") #有�response,可能是不正確的.所以要檢查status_code,是否回應成功        
        if response.status_code == 200:
            print("成功傳送,status_code==200")
        else:
            print("server回應有問題")
            print(f'status_code:{response.status_code}')
        response.close() #有response就要關閉
    
    
connect()
time1 = Timer()
time1.init(period=10000,callback=callback1)