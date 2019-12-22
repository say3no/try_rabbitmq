
#!/usr/bin/env python
import pika
import sys
QUEUE_NAME = 'task_queue'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.exchange_declare(exchange='logs', exchange_type='fanout')

message = ''.join(sys.argv[1:]) or "Info: Hello World!"

channel.basic_publish(exchange='logs', routing_key='', body=message)

print("[x] Sent %r" % message)

connection.close()
