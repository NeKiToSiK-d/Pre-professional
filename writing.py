#!usr/bin/python
from influxdb import InfluxDBClient


client = InfluxDBClient(host='localhost', port=8086)
client.create_database('BinarySensor')
client.switch_database('BinarySensor')
json_body = [
    {
        "measurement": "BinarySensor",
        "tags": {
            "user": "Platon",
            "SensorId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": "2018-03-28T8:01:00Z",
        "fields": {
            "TurnOnTime": 127
        }
    },
    {
        "measurement": "BinarySensor",
        "tags": {
            "user": "Nikita",
            "SensorId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": "2018-03-29T8:04:00Z",
        "fields": {
            "TurnOnTime": 132
        }
    },
    {
        "measurement": "BinarySensor",
        "tags": {
            "user": "Kirill",
            "SensorId": "6c89f539-71c6-490d-a28d-6c5d84c0ee2f"
        },
        "time": "2018-03-30T8:02:00Z",
        "fields": {
            "TurnOnTime": 129
        }
    }
]
client.write_points(json_body)
