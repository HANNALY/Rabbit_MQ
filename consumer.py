# Rabbit_MQ

#!/usr/bin/env python
import pika

credentials = pika.PlainCredentials('login', 'hasło')
parameters = pika.ConnectionParameters('nazwa_serwera',
                                       5672,
                                       '/',
                                       credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

queue_name='nazwa_kolejki'
print(' [*] Waiting for logs. To exit press CTRL+C')

def callback(ch, method, properties, body):
    print(" [x] %r" % body)

channel.basic_consume(callback,
                      queue=queue_name,
                      no_ack=True)

