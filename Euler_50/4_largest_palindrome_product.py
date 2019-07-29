import time

'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.'''

def largest_palindrome_product(test): 
  print('lpp')

while True: 
  a_number = int(input('Find the largest palindrome product of a number: '))

  start = time.time()
  print(largest_prime_factor(a_number))
  end = time.time()
  print('Processed in ', end - start, 'seconds')

# b = primes.Primer() # create a new primer object
# print(b.cache)
