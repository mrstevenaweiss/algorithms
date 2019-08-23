
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

def largest_prime_factor(test):
    nums = []
    # test = 13195
    divider = 2
  
    while divider <= test:
      if test % divider != 0:
        divider += 1
      else:
        test = test // divider
        nums.append(divider)
    return nums[-1]
  
def getDivisors(n): 
    i = 1
    divisors = []
    while i <= n : 
        if (n % i==0) : 
            divisors.append(i) 
        i = i + 1
    return divisors

start = time.time()
#function here
end = time.time()
print('Processed in ', end - start, 'seconds')


