'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''

#0. Build a helper to check if a number is prime...
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

primes = []
#0a. Check if the number itself is prime, else...
def largest_prime_factor(number):
    if is_prime(number) == True:
        return number, 'is the largest prime factor'
    else: 
    #1. Get all the factors a number
        factors = []
        num = number
        midpoint = int(num/2)+1
        for i in range(2, midpoint):
            if num % i == 0:
                factors.append(i)

    #2. Pass all the factors to the helper and append to a list        
        for x in factors:
            if is_prime(x) == True:
                primes.append(x)
        print( max(primes) )

#3. Take the max of a list...   
while True:
    print('Check if largest prime factor of a number: ')
    num = int(input(">>>  "))
    largest_prime_factor(num)
