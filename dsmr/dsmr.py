#!/usr/bin/env python3

from dsmr_parser import telegram_specifications
from dsmr_parser.clients import SerialReader, SERIAL_SETTINGS_V5
from dsmr_parser.objects import CosemObject, MBusObject, Telegram
from dsmr_parser.parsers import TelegramParser
import os, random, time
import yaml
import paho.mqtt.client as mqtt

valuesOfInterest = os.getenv("VALUES_OF_INTEREST", "CURRENT_ELECTRICITY_USAGE,ELECTRICITY_USED_TARIFF_ALL,HOURLY_GAS_METER_READING").split(',')
topicStart=os.getenv('MQTT_TOPICSTART', "home/smart_meter/")

# Set the parameters for dsmr_parser
serial_reader = SerialReader(
    device=os.getenv('DSMR_DEVICE', '/dev/ttyUSB0'),
    serial_settings=SERIAL_SETTINGS_V5,
    telegram_specification=telegram_specifications.V5
)

# Initiate the mqtt connection
client = mqtt.Client(os.getenv('MQTT_CLIENT_NAME', "sim"))
if os.getenv('MQTT_USER'):
    client.username_pw_set(os.getenv('MQTT_USER'), password=os.getenv('MQTT_PASSWORD', ""))
client.reconnect_delay_set(min_delay=1, max_delay=120)
client.connect(os.getenv('MQTT_BROKER', "mqtt"))

# Get all the telegram's values into a dictionary
for telegram in serial_reader.read_as_object():
    for attr, value in telegram:
        if (attr in valuesOfInterest):
            topic = topicStart + attr
            client.publish(topic, float(value.value))