#!usr/bin/python
from influxdb import InfluxDBClient
from datetime import datetime


client = InfluxDBClient(host='localhost', port=8086)
client.create_database('BinarySensor')
client.switch_database('BinarySensor')
json_body = [
    {
        "measurement": "BinarySensor",
        "tags": {
            "user": "Platon",
            "SensorId": "A1"
        },
        "time": datetime.now(),
        "fields": {
            "TurnOnTime": 127
        }
    },
    {
        "measurement": "BinarySensor",
        "tags": {
            "user": "Nikita",
            "SensorId": "A2"
        },
        "time": datetime.now(),
        "fields": {
            "TurnOnTime": 132
        }
    },
    {
        "measurement": "BinarySensor",
        "tags": {
            "user": "Kirill",
            "SensorId": "A3"
        },
        "time": datetime.now(),
        "fields": {
            "TurnOnTime": 129
        }
    }
]
client.write_points(json_body)
