#simple thread

import threading
import time

def task():
    print("Thread started")
    time.sleep(1)
    print("thread finished")

t = threading.Thread(target= task)
t.start()
t.join()

print("Thread terminated")