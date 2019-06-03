from multiprocessing import Process
import time
from redis import Redis


def pub(myredis):
    for n in range(10):
        myredis.publish('channel', 'blah %d' % n)
        time.sleep(5)


def sub(myredis, name):
    pubsub = myredis.pubsub()
    pubsub.subscribe(['channel'])
    for item in pubsub.listen():
        print('{} : {}'.format(name, item['data']))


def start_automation():
    print('hello')
    myredis = Redis(host='redis', port=6379)
    Process(target=pub, args=(myredis,)).start()
    Process(target=sub, args=(myredis,'reader1')).start()
    Process(target=sub, args=(myredis,'reader2')).start()