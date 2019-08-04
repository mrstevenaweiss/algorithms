
import time
import primer

'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.
What is the 10 001st prime number?

'''
# def get_prime():
primes_list = primer.Primer()

# for i in range(1000000):
#     primes_list.is_prime(i)
print(primes_list.cache, '\n')

start = time.time()
print(primes_list.cache[2])
end = time.time()
print('Processed in ', end - start, 'seconds')








            
