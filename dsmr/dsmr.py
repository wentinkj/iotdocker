#!/usr/bin/env python3

from dsmr_parser import telegram_specifications
from dsmr_parser.clients import SerialReader, SERIAL_SETTINGS_V5
from dsmr_parser.objects import CosemObject, MBusObject, Telegram
from dsmr_parser.parsers import TelegramParser
import os
import yaml
import paho.mqtt.client as mqtt

# Load the config file
with open('config.yaml') as file:
    config = yaml.load(file, Loader=yaml.FullLoader)

# Set the parameters for dsmr_parser
serial_reader = SerialReader(
    device='/dev/ttyUSB0',
    serial_settings=SERIAL_SETTINGS_V5,
    telegram_specification=telegram_specifications.V5
)

# Initiate the mqtt connection
client = mqtt.Client(config['mqtt_client_name'])
if 'mqtt_username' in config:
    client.username_pw_set(config['mqtt_username'], password=config['mqtt_password'])
client.reconnect_delay_set(min_delay=1, max_delay=120)
client.connect(config['mqtt_broker_address'])

# Get all the telegram's values into a dictionary
for telegram in serial_reader.read_as_object():
    for attr, value in telegram:
        if (attr in config['values_of_interest']):
            topic = config['topic'] + '/' + attr
            client.publish(topic, float(value.value))