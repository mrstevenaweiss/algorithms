"""
The Fibonacci sequence is defined by the recurrence relation:

Fn = Fn−1 + Fn−2, where F1 = 1 and F2 = 1.
Hence the first 12 terms will be:

F1 = 1
F2 = 1
F3 = 2
F4 = 3
F5 = 5
F6 = 8
F7 = 13
F8 = 21
F9 = 34
F10 = 55
F11 = 89
F12 = 144
The 12th term, F12, is the first term to contain three digits.

What is the index of the first term in the Fibonacci sequence to contain 1000 digits?

"""
import time
import math
from decimal import *
getcontext().prec = 1000

five  = Decimal(5).sqrt()
first = 1 / five
second = (1 + five) / 2
third = (1 - five) / 2

# print(five)

def len_closed_fib(n):
    body = (second**n) - (third**n)
    fib = int(first * body)
    return fib, len( str(fib) )

def get_thousand():
    length = 0
    number = 0
    index = 0

    while length != 1000:
        number, length = len_closed_fib(index)
        index += 1
    print(number, index-1)    

start = time.time()
# print(closed_fib(12))
get_thousand()
end = time.time()
print('Processed in ', end - start, 'seconds')