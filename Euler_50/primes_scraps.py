import time

# def memoize(func):
#     cache = dict()

#     def memoized_func(*args):
#         if args in cache:
#             return cache[args]
#         result = func(*args)
#         cache[args] = result
#         return result

#     return memoized_func

# def fibonacci(n):
#     if n == 0:
#         return 0
#     elif n == 1:
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)

# start = time.time()
# print(fibonacci(32))
# end = time.time()
# print('Processed in ', end - start, 'seconds')

# start = time.time()
# print(memoize (fibonacci(32)) )
# end = time.time()
# print('Processed in ', end - start, 'seconds')

# start = time.time()
# memoized_fibonacci = memoize(fibonacci)
# print(memoized_fibonacci(32) )
# end = time.time()
# print('Processed in ', end - start, 'seconds')

# print(memoized_fibonacci.__closure__[0].cell_contents)


# from functools import lru_cache

# @lru_cache(maxsize=32)
# def fib(n):
#     if n < 2:
#         return n
#     return fib(n-1) + fib(n-2)

# fibs = [fib(n) for n in range(50)]

# start = time.time()
# print(fibs[100])

# end = time.time()
# print('Processed in ', end - start, 'seconds')