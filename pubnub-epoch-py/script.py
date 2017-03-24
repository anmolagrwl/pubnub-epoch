from random import randint
import threading
from pubnub import Pubnub
from datetime import datetime
import time

pn = 0

def main():
    global pn
    pn = Pubnub(publish_key="demo", subscribe_key="demo", ssl_on=False)
    loop()

def loop():
    threading.Timer(1, loop).start()
    num = randint(0, 10)
    print(num)
    dt = datetime.now()
    timestamp = int((time.mktime(dt.timetuple()) + dt.microsecond/1000000.0)*1000)
    object = dict(time=timestamp, y=num)
    pn.publish(channel="epoch-pubnub", message=object)

if __name__ == "__main__":
    main()
