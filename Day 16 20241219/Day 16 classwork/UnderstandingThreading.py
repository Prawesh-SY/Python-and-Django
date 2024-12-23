# Learn Threading in Python
import threading
import time

def task_1():
    time.sleep(5)
    print("Task One Ongoing......")
    time.sleep(5)

def task_2():
    time.sleep(5)
    print("Task Two Onging........")
    time.sleep(5)

t1=threading.Thread(target=task_1)
t1.start()
# t1.join()

t2=threading.Thread(target=task_2)
t2.start()

task_1()
task_2()
