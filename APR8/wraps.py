from functools import wraps

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f"Calling function: {func.__name__}")
        result = func(*args, **kwargs)
        print(f"Function {func.__name__} finished")
        return result
    return wrapper


@logger
def greet(name):
    """Greets a person"""
    return f"Hello, {name}!"


print(greet("Tarak"))


print(greet.__name__)   
print(greet.__doc__)   