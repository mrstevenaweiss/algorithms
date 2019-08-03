
import time
import primes

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

'''
def get_prime(X):
    x = primes.Primes()
  

start = time.time()

get_prime(5)

end = time.time()
print('Processed in ', end - start, 'seconds')








            
