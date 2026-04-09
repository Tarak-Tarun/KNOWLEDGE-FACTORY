import time
from functools import wraps
def timer(func):
    @wraps(func)
    def wrapper():
        start=time.time()
        func()
        end=time.time()
        print(f"Execution time: {end-start} seconds")
    return wrapper
@timer
def say_hello():
    print("Hello!")
    time.sleep(2)
say_hello()