from functools import wraps
def my(func):
    @wraps(func)
    def sample():
        print("Starting Process.")
        func()
        print("Something is happening after the function is called.")

    return sample


@my
def say_hello():
    print("Logging in!")
    print(say_hello.__name__)
    print(say_hello.__doc__)


say_hello()
