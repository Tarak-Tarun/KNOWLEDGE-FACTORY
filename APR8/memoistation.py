import time
from functools import lru_cache, wraps


def decorator(func):
    @lru_cache(maxsize=None)
    def fibonacci(a):
        print(f"Calculating Fibonacci of {a}")
        start = time.time()
        i, j = 0, 1
        for i in range(1, a + 1):
            i, j = j, i + j
        end = time.time()
        print(f"Execution time: {end-start} seconds")
        return i

    return fibonacci


@decorator
def fibonacci(n):
    pass


if __name__ == "__main__":
    print(fibonacci(30))
    print(fibonacci(30))
    print(fibonacci.__name__)
