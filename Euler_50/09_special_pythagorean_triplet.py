
import time 
"""
Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 5^2  ==> 9 + 16 = 25.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.

a+b+c (unsquared must == 1000)  &&  must be pythagorean triplet...
"""

bound = 500
pythags = []
Cs = []

#possible c^2
for i in range(bound):
    Cs.append(i**2)
# print(Cs)

def triplet():
    for a in range(1, bound):
        for b in range(1, bound):
            square_sum = a**2 + b**2
            if square_sum in Cs:
                c = Cs.index(square_sum)
                if a+b+c == 1000: 
                    print('pythag triplet', a, b, '==', c, '||', Cs[a], '+', Cs[b], '==', square_sum)
                    print('solution', a*b*c)
                break

start = time.time()
triplet()
end = time.time()
print('Processed in ', end - start, 'seconds')

print(200+375+425)
print(200*375*425)