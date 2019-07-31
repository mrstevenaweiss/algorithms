import time

def smallest_multiple():
    print('SM')

start = time.time()
smallest_multiple()
end = time.time()
print('Processed in ', end - start, 'seconds')

# def tests():
#   assert multiply([1, 2, 3, 4]) == 23, 'multiply failed'
#   assert multiply([1, 2, 3, 4]) == 24, 'multiply failed'
#   return 'pass'

# print(tests())