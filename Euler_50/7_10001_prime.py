
import time

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

'''
primes = []

def is_prime(n):
  if n == 2 or n == 3: return True
  if n < 2 or n%2 == 0: return False
  if n < 9: return True
  if n%3 == 0: return False
  r = int(n**0.5)
  f = 5
  while f <= r:
    # print('\t',f)
    if n%f == 0: return False
    if n%(f+2) == 0: return False
    f += 6
  return True

def get_primes(a_num):
    for i in range(2, a_num):
        prime_bool = is_prime(i)
        if prime_bool == True:
            primes.append(i)
    return primes

start = time.time()
print(get_primes(2000000))
end = time.time()
print('Processed in ', end - start, 'seconds')








            
