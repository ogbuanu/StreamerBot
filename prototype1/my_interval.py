import threading
import multiprocessing

def setInterval(func,time):
    e = multiprocessing.Event()
    while not e.wait(time):
        func()