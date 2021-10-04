from random import randint
from time import sleep

timeout = randint(20, 30)

def short_nap():
    sleep(randint(1, 2))
