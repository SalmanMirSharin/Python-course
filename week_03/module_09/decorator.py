import math
import time
def timer(func):
    def inner(*args,**kwarg):
        print('Time Start')
        start = time.time()
        func(*args,**kwarg)
        end = time.time()
        print(f'Time End, Total time taken: {end-start}')
    return inner
@timer
def get_factorial(n):
    result = math.factorial(n)
    print(f'factorial of {n} is: {result}')

# timer(get_factorial)()
get_factorial(n=5) 