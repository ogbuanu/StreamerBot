from api import *
from my_interval import setInterval


def func():
    for _ in range(10):
        bot = Streamer()
        bot()
        print("visiting site... Done!")

setInterval(func,5)