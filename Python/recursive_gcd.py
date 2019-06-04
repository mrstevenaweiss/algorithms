

def gcd(a, b):
    if a == 0:
        return b
    else:
        return gcd(b % a, a)

while True:
    print("Calculate the greatest common divisor for two numbers, a & b. 'q' to quit, hit 'Enter' to see \n")

    print('Type first number: ')
    a = int(input())
    print('Type second number: ')
    b = int(input())

    if a == 'q' or b == 'q':
        break
    else:
        answer = gcd(a, b)
        print("Your answer is", answer, "\n")
