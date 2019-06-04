# # ALGORITHM - COLLATZ SEQUENCE
#
def collatz(number):
    if number > 1:
        while number != 1:
            if number % 2 == 0:
                even = number // 2
                print(even)
                number = even

            elif number % 2 == 1:
                odd = 3 * number + 1
                print(odd)
                number = odd
    else:
        print('Come on bruh')


# RUN PROGRAM // TYPE PYTHON3 COLLATZ.PY
while True:
    print('\n')
    print("Type a number > 1 to see the Collatz Sequence: (type 'q' to quit) \n")
    n = input()
    if str(n) == 'q':
        print('Thank you.')
        break
    else:
        try:
            collatz(int(n))
        except ValueError:
                print('Non-Integer entered, program will exit')
