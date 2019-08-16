import time
import math
"""
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! icds 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

"""
def fast_fact(N):
    return math.factorial(N)

def add_fact_digits(N):
    number = str(fast_fact(N))
    nombres = [int(i) for i in list(number)] 
    return sum(nombres)

start = time.time()
print ( add_fact_digits(100) )
end = time.time()
print('Processed in ', end - start, 'seconds')

