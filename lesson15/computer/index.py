import paho.mqtt.client as mqtt
from datetime import datetime
import os,csv

def record(topic:str,value:int | float):
    '''
    #檢查是否有data資料夾,沒有就建立data資料夾
    #取得今天日期,如果沒有今天日期.csv,就建立一個全新的今天日期.csv
    #將參數r的資料,儲存進入csv檔案內
    #parameters topic:str -> 這是訂閱的topic
    #parameters value:int -> 這是訂閱的value
    '''
    root_dir = os.getcwd()
    data_dir = os.path.join(root_dir, 'data')
    if not os.path.isdir(data_dir):    
            os.mkdir('data')
    
    today = datetime.today()
    current_str = today.strftime("%Y-%m-%d %H:%M:%S")
    date = today.strftime("%Y-%m-%d")
    filename = date + ".csv"
    #get_file_abspath
    full_path = os.path.join(data_dir,filename)
    if not os.path.exists(full_path):
        #沒有這個檔,建立檔案
        print('沒有這個檔')
        with open(full_path,mode='w',encoding='utf-8',newline='') as file:
            file.write('時間,設備,值\n')
    
    with open(full_path, mode='a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        writer.writerow([current_str,topic,value])


def on_connect(client, userdata, flags, reason_code, properties):
    #連線bloker成功時,只會執行一次
    client.subscribe("SA-01/#")

def on_message(client, userdata, msg):
    global led_origin_value
    global temperature_origin_value

    topic = msg.topic
    value = msg.payload.decode()
    if topic == 'SA-01/LED_LEVEL':
        led_value = int(value)
        if led_value != led_origin_value:
            led_origin_value = led_value
            record(topic,led_value)
    
    if topic == 'SA-01/TEMPERATURE':
        temperature_value = float(value)
        if temperature_origin_value != temperature_value:           
           temperature_origin_value = temperature_value
           record(topic,temperature_value)
        
def main():
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    # 設定用戶名和密碼
    username = "pi"  # 替換為您的用戶名
    password = "raspberry"  # 替換為您的密碼
    client.username_pw_set(username, password)
    client.on_connect = on_connect
    client.on_message = on_message 
    client.connect("192.168.0.252", 1883, 60)
    client.loop_forever()


if __name__ == "__main__":
    led_origin_value = 0
    temperature_origin_value = 0.0
    main()