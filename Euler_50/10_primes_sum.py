import time 
import primes_dict

# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.
# Find the sum of all the primes below two million.

primes = primes_dict.primes

def sum_primes():
    sums = 0
    for i in range(len(primes)):
        sums = sums + primes[i]
    print(sums)

start = time.time()
sum_primes()
end = time.time()
print('Loop Processed in ', end - start, 'seconds')

start = time.time()
print(sum(primes))
end = time.time()
print('Built-in Processed in ', end - start, 'seconds')