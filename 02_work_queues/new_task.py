
#!/usr/bin/env python
import pika
import sys
QUEUE_NAME = 'task_queue'

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.queue_declare(queue=QUEUE_NAME, durable=True)
message = ''.join(sys.argv[1:]) or "Hello World!"
channel.basic_publish(exchange='',
                      routing_key=QUEUE_NAME,
                      body=message,
                      properties=pika.BasicProperties(delivery_mode=2))
print("[x] Sent %r" % message)

connection.close()
