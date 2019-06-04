

def factorial(n):
    if n < 2:
        return 1
    else:
        return n * factorial(n-1)

while True:
    print("Calculate factorial of n? 'q' to quit, hit 'Enter' to see \n")
    fact = int(input())
    if fact == 'q':
        break
    else:
        answer = factorial(fact)
        print("Your answer is", answer, "\n")
