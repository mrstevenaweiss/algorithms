
import time
'''
The sum of the squares of the first ten natural numbers is,
1^2 + 2^2 + ... + 10^2 = 385

The square of the sum of the first ten natural numbers is,
(1 + 2 + ... + 10)2 = 55^2 = 3025

Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025 − 385 = 2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

'''
def gauss_add(N):    
    return (N*(N+1)) /  2

def sum_squares(N):
    sum = 0
    for i in range(1, N+1):
        # print(i)
        sum += (i**2)
    return sum

def sum_square_diff():
    N = 100

    print('gauss squared', int(gauss_add(N)**2))
    print( 'sum of', N, 'squares', sum_squares(N) )
    
    answer = gauss_add(N)**2 - sum_squares(N)
    print('answer', answer)
  

start = time.time()
sum_square_diff()
end = time.time()
print('Processed in ', end - start, 'seconds')








            
