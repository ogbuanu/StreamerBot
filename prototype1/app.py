from api import *
from my_interval import setInterval


def func():
    bot = Streamer()
    for _ in range(10):
        bot()

setInterval(func,30)