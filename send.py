# Rabbit_MQ

#!/usr/bin/env python
import pika
import datetime
now = datetime.datetime.now()

#print ("Current date and time : ")
#print (now.strftime("%Y-%m-%d %H:%M:%S"))

#komunikat = now.strftime("Komunikat nadano o %Y-%m-%d %H:%M:%S")
komunikat = "Hello World!"

credentials = pika.PlainCredentials('login', 'hasło')
parameters = pika.ConnectionParameters('nazwa_serwera',
                                       5672,
                                       '/',
                                       credentials)

connection = pika.BlockingConnection(parameters)
channel = connection.channel()

channel.queue_declare(queue='nawa_kolejki',durable=True)
