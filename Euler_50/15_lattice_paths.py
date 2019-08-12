import time
import  math

"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.
How many such routes are there through a 20×20 grid?

This is a combination problem.

𝐶(𝑛,𝑟)=𝑛!(𝑟!(𝑛−𝑟)!)

Combination
The number of ways to choose a sample of r elements from a set of n distinct objects where order does not matter and replacements are not allowed.
n = the set or population
r = subset of n or sample set

"""
def fast_fact(N):
    return math.factorial(N)

def combination(N, R):
    print('combination: n! / (𝑟! * (𝑛−𝑟)!)')
    N_R = fast_fact(N-R)
    print('n-r!', N_R)

    N = fast_fact(N)
    print('n!', N)
    R = fast_fact(R)
    print('r!', R)

    return N // (R * N_R)  

start = time.time()
print('answer', combination(40, 20) )
end = time.time()
print('Processed in ', end - start, 'seconds')
