from functools import wraps
def my_decorator(func):
    @wraps(func)
    def wrapper():
        print("Something is happening before the function is called.")
        func()
        print("Something is happening after the function is called.")
    return wrapper
@my_decorator
def say_hello():
    """This function says hello""" #
    #Decription of the function
    print("Hello!")
print(say_hello.__name__)
print(say_hello.__doc__)