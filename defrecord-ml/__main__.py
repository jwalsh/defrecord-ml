import sys
import os
import signal
import logging.config
import yaml
import json
from threading import Thread
from kafka import KafkaProducer, KafkaConsumer

def main(args):
    project_names = ['banking_target', 'iris', 'titanic', 'boston', 'banking_target']
    for project_name in project_names:
        try:
            _setup_kafka_consumer(project_name)
        except:
            pass

def _setup_kafka_consumer(project_name):
    print('Running Consumer {}..'.format(project_name))
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
    print('Running Consumer..')
    main(sys.argv[1:])
