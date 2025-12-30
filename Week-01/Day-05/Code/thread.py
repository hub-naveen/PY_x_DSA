from threading import Thread
import time

def task():
    time.sleep(1)
    print("Task done")

t1 = Thread(target=task)
t1.start()
t1.join()
