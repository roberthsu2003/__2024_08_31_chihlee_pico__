from tools import connect,reconnect
import utime
from umqtt.simple import MQTTClient
from machine import Timer

   
def callback1(t:Timer):
    global counter    
    mqtt_host = "10.170.1.218"    
    mqtt_publish_topic = "a01/device1"  # The MQTT topic for your Adafruit IO Feed

    # Initialize our MQTTClient and connect to the MQTT server
    mqtt_client_id = "pico1"
    user='pi'
    password='raspberry'
    mqtt_client = MQTTClient(
        client_id=mqtt_client_id,
        server=mqtt_host,
        user=user,
        password=password
        )    
    mqtt_client.connect()
    
    try:       
        
        counter += .8        
        # Publish the data to the topic!
        print(f'Publish {counter:.2f}')
        mqtt_client.publish(mqtt_publish_topic, str(counter))
            
            
            
    except Exception as e:
        print(f'Failed to publish message: {e}')
    finally:
        mqtt_client.disconnect()    
    
    
    
    
connect()
counter = 0
time1 = Timer(period=3000, mode=Timer.PERIODIC, callback=lambda t:callback1(t))
