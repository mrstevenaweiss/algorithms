

def fib(n):
    if n <= 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

while True:
    print("Input a number between 0 and 35 to see its Fibonacci Sequence: (type 'q' to quit) \n")
    n = input()
    if str(n) == 'q':
        print('Thank you.')
        break
    elif int(n) > 35:
        print('Your number is too large.  Try again. \n')
    else:
        print(fib(int(n)), "\n")
