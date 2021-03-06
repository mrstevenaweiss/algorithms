import time
import primes_dict
import math
"""
The sequence of triangle numbers is generated by adding the natural numbers. 
So the 7th triangle number would be 1 + 2 + 3 + 4 + 5 + 6 + 7 = 28. 
The first ten terms would be:

[1, 3, 6, 10, 15, 21, 28, 36, 45, 55]

Let us list the factors of the first seven triangle numbers:

 1: 1
 3: 1,3
 6: 1,2,3,6
10: 1,2,5,10
15: 1,3,5,15
21: 1,3,7,21
28: 1,2,4,7,14,28
We can see that 28 is the first triangle number to have over five divisors.

What is the value of the first triangle number to have over five hundred divisors?

algo strat
1. get X amount of triangle numbers
2. get the prime factorization of this number
3. multiply something something...

use the index of the first instane of 500 divisors to grab the index of triangles
"""
primes = primes_dict.primes

def total_divisors(hash):
    num = 1
    for k in hash:
        num *= (hash[k] + 1)
    return num

def count_prime_factors(N):
    """ Gets all prime factors for given number & passes down result to calculate the divisors for N """
    number = N
    factors = {}
    adder = 0

    while N != 1:   
        divider = primes[adder]
        if N % divider == 0:
            if divider in factors: 
                factors[divider] += 1
            else:
                factors[divider] = 1
            N = N // divider
        else: 
            adder += 1
    # print(  '{0}: {1} of number {2}'.format('prime factors', factors, number) )
    return total_divisors(factors)

# print(count_prime_factors(137373600*2))

def triangular():
    """ This loop processes the first 20000 triangle numbers """

    tris = {} #20000th triangle number is 200010000
    max = 0
    i = 0
    
    for i in range(1, 20000+1):
        # calculates triangle numbers 
        triangle_number = int( i*(i+1) / 2 )

        # returns divisors for first 20000 triangle numbers
        max = count_prime_factors(triangle_number)
        if max >= 500:
            print(triangle_number, max)
        
        # stores first 20,000 triangle numbers w their respective divisors
        tris[triangle_number] = count_prime_factors(triangle_number)
        i += 1
    # print(tris)

start = time.time()
triangular()
end = time.time()
print('Built-in Processed in ', end - start, 'seconds')
