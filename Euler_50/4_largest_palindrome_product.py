import time
'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''

def is_palindrome(numbers):
  numbers = str(numbers)
  reversed_string = numbers[::-1]
  return numbers == reversed_string

def largest_palindrome_product(): #test
  first = 999
  second = 999
  number = 1
  pal = False

  while pal == False:
    number = first * second
    pal = is_palindrome(number)
    second = second - 1
    if second == 100:
      second = 999
      first = first - 1

  print(pal, first, second, number)

start = time.time()
largest_palindrome_product()
end = time.time()
print('Processed in ', end - start, 'seconds')

# def tests():
#   assert multiply([1, 2, 3, 4]) == 23, 'multiply failed'
#   assert multiply([1, 2, 3, 4]) == 24, 'multiply failed'
#   return 'pass'

# print(tests())
