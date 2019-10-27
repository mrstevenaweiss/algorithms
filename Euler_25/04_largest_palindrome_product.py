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
  row_loop = 1
  different  = 0

  while pal == False:
    number = first * second
    pal = is_palindrome(number)
    second = second - 1
    print(row_loop, 'first', first, 'second', second, number)
    if row_loop == (99-different):
      second = first
      first = first - 1
      row_loop = 0
      different += 1
    row_loop += 1

  # print(pal, first, second, number)


start = time.time()
largest_palindrome_product()
end = time.time()
print('Processed in ', end - start, 'seconds')

# def tests():
#   assert multiply([1, 2, 3, 4]) == 23, 'multiply failed'
#   assert multiply([1, 2, 3, 4]) == 24, 'multiply failed'
#   return 'pass'

# print(tests())
