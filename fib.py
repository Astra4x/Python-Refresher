#fib.py

from functools import lru_cache
from time import time

def timer(func):  
    def wrap_func(*args, **kwargs): 
        start = time() 
        result = func(*args, **kwargs) 
        end = time() 
        print(f'Finished in {(end-start):.8f}s: f({args[0]}) -> {func(*args, **kwargs)}') 
        return result 
    return wrap_func 

@lru_cache
@timer
def fib(n: int) -> int:
    if n == 0:
        return 0
    elif n == 1:
        return 1
    return fib(n-1) + fib(n-2)
    

if __name__ == "__main__":
    fib(100)