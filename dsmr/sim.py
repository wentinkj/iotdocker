#!/usr/bin/env python3

import os, random, time
import yaml
import paho.mqtt.client as mqtt

valuesOfInterest = os.getenv("VALUES_OF_INTEREST", "CURRENT_ELECTRICITY_USAGE,ELECTRICITY_USED_TARIFF_ALL,HOURLY_GAS_METER_READING").split(',')
topicStart=os.getenv('MQTT_TOPICSTART', "home/smart_meter/")

# Initiate the mqtt connection
client = mqtt.Client(os.getenv('MQTT_CLIENT_NAME', "sim"))
if os.getenv('MQTT_USER'):
    client.username_pw_set(os.getenv('MQTT_USER'), password=os.getenv('MQTT_PASSWORD', ""))
client.reconnect_delay_set(min_delay=1, max_delay=120)
client.connect(os.getenv('MQTT_BROKER', "mqtt"))

# random floating values for all values of interest/topics
while True:
    for attr in valuesOfInterest:
        topic = topicStart + attr
        value = random.uniform(1.5, 1000.98)
        client.publish(topic, float(value))
    time.sleep(1)