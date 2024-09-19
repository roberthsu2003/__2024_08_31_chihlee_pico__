#!/usr/bin/env python3
# SPDX-FileCopyrightText: 2024 Volodymyr Shymanskyy for Blynk Technologies Inc.
# SPDX-License-Identifier: Apache-2.0
#
# The software is provided "as is", without any warranties or guarantees (explicit or implied).
# This includes no assurances about being fit for any specific purpose.

import time
import ssl
import config, demo

from paho.mqtt.client import Client, CallbackAPIVersion
from urllib.parse import urlparse

mqtt = Client(CallbackAPIVersion.VERSION2)
device = demo.Device(mqtt)

def on_connect(mqtt, obj, flags, reason_code, properties):
    if reason_code == 0:
        print("Connected [secure]")
        mqtt.subscribe("downlink/#", qos=0)
        device.connected()
    elif reason_code == "Bad user name or password":
        print("Invalid BLYNK_AUTH_TOKEN")
        mqtt.disconnect()
    else:
        raise Exception(f"MQTT connection error: {reason_code}")

def on_message(mqtt, obj, msg):
    payload = msg.payload.decode("utf-8")
    topic = msg.topic
    if topic == "downlink/redirect":
        url = urlparse(payload)
        print("Redirecting...")
        mqtt.connect_async(url.hostname, url.port, 45)
    elif topic == "downlink/reboot":
        print("Reboot command received!")
    elif topic == "downlink/ping":
        pass  # MQTT client library automagically sends the QOS1 response
    elif topic == "downlink/diag":
        print("Server says:", payload)
    else:
        print(f"Got {topic}, value: {payload}")
        device.process_message(topic, payload)

def main():
    mqtt.tls_set(tls_version=ssl.PROTOCOL_TLSv1_2)
    mqtt.on_connect = on_connect
    mqtt.on_message = on_message
    mqtt.username_pw_set("device", config.BLYNK_AUTH_TOKEN)
    mqtt.connect_async(config.BLYNK_MQTT_BROKER, 8883, 45)
    mqtt.loop_start()

    while True:
        device.update()
        time.sleep(1)

if __name__ == "__main__":
    main()