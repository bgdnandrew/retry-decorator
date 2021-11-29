from retry import retry
from random import random 
import time
from functools import wraps

# Original decorator
#_________________________________________________
# @retry(tries=10, delay=3)
# def toggler(chance):
#     x = random()
#     print('x', x)
#     if x <= chance:
#         assert False

# toggler(0.75)

# Implementing the decorator
#_________________________________________________
def self_made_retry(tries, delay):
    def intermediary(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            tries_wrapper = 0
            while(tries_wrapper < tries):
                try:
                    return func(*args, **kwargs)
                except: 
                    print('too small')
                    time.sleep(delay)
                    tries_wrapper += 1
        return wrapper
    return intermediary
                

@self_made_retry(tries=10, delay=3)
def toggler(chance):
    x = random()
    print('x', x)
    if x <= chance:
        assert False

toggler(0.75)