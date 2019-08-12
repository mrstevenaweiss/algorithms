
import time

def reverse(string): 
    string = string[::-1] 
    return string 

def isqrt(n):
    "Integer square root (rounds down)."
    return int(n ** 0.5)


def multiply(numbers):
    "Multiply all the numbers together."
    result = 1
    for n in numbers:
        result *= n
    return result


start = time.time()
#function here
end = time.time()
print('Processed in ', end - start, 'seconds')


