import time

'''
The prime factors of 13195 are 5, 7, 13 and 29.
What is the largest prime factor of the number 600851475143 ?
'''
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

while True: 
  a_number = int(input('Find the largest prime factor of a number: '))

  start = time.time()
  print(largest_prime_factor(a_number))
  end = time.time()
  print('Processed in ', end - start, 'seconds')

# b = primes.Primer() # create a new primer object
# print(b.cache)
