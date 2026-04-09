import time
from functools import wraps
def timer(func):
    @wraps(func)
    def wrapper():
        print("Starting the function execution.")
        start=time.time()
        func()
        print("Function execution completed.")
        end=time.time()
        print(f"Execution time: {end-start} seconds")
    return wrapper
@timer
def say_hello():
   for i in range(100):
        print("Hello!")

say_hello()