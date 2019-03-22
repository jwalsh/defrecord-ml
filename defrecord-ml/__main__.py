import sys
import os
import signal
import logging.config
import yaml
import json
from threading import Thread
from kafka import KafkaProducer, KafkaConsumer

# import defrecord_ml_custom_transformers
# import preprocessors

def main(args):
    project_names = [
        'banking-customer_target',
        'building_heating-load'
        'car_price',
        'iris_class',
        'titanic-passenger_survived',
        'wine_quality',
    ]
    for project_name in project_names:
        try:
            _setup_kafka_consumer(project_name)
        except:
            pass

def _setup_kafka_consumer(project_name):
    print('{}'.format(project_name))
    parsed_records = []
    topic_name = 'raw_{}_input'.format(project_name)
    parsed_topic_name = 'parsed_{}_input'.format(project_name)

    consumer = KafkaConsumer(topic_name,
                             auto_offset_reset='earliest',
                             bootstrap_servers=['localhost:9092'],
                             api_version=(0, 10),
                             consumer_timeout_ms=1000)
    for msg in consumer:
        parsed_records.append(msg.value)
    consumer.close()
    sleep(5)

if __name__ == '__main__':
    # signal.signal(signal.SIGTERM)
    status = main(sys.argv[1:])
    print('Exit status: {}'.format(status))
    sys.exit(status)
