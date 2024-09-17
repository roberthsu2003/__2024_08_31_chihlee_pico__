"""
A small example subscriber
"""
import paho.mqtt.client as mqtt

# Define the callback function for when a message is received
def on_message(mosq, obj, msg):
    print("topic:{0},payload:{1},qos:{2}".format(msg.topic,msg.payload.decode('utf-8'),msg.qos)) #msg.payload是binary string
    
# Define the callback function for when the client connects to the broker
def on_connect(client, userdata, flags, rc,properties=None):
    print(f"Connected with result code {rc}")
    # Subscribe to the topic once connected
    client.subscribe("a01/#")
    



if __name__ == '__main__':
    client = mqtt.Client(mqtt.CallbackAPIVersion.VERSION2)
    client.on_message = on_message
    client.on_connect = on_connect
    
    # Set user ID and password
    client.username_pw_set("pi","raspberry")

	#SSL連線
    #client.tls_set('root.ca', certfile='c1.crt', keyfile='c1.key')
    
    # Connect to the broker (replace 'broker_address' with the address of your MQTT broker)
    client.connect("10.170.1.218", 1883, 60)
    client.loop_forever()
