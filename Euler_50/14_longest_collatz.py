import time 

"""The following iterative sequence is defined for the set of positive integers:

n → n/2 (n is even)
n → 3n + 1 (n is odd)

Using the rule above and starting with 13, we generate the following sequence:

13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

Which starting number, under one million, produces the longest chain?

NOTE: Once the chain starts the terms are allowed to go above one million.

answer: 837799
"""

# this is an incredibly inefficient checker..but works.... dict?

# 1. test a collatz sequence of given N
# 2. use a list to count lengths of a particular number, return the associated number
# 2a. data struct could be a list or dict

def collatz_sequence(N):
    # print('in col seq', N)
    col_seq = []
    
    while N != 1:
        col_seq.append(N)
        if N % 2 == 0:
            N = N // 2 
        elif N % 2  == 1:
            N = 3*N + 1     
    return len(col_seq)+1

def collatz():
    a_num = 0
    length = 0
    for num in range(1, 1000001):   
             
        col_size = collatz_sequence(num)
        # print('num', num, 'col size', col_size, 'length', length)
        if col_size > length:
            a_num = num
            length = col_size
            # print('length', length)
    print('final number', a_num, 'length of col', length)

start = time.time()
collatz()
end = time.time()
print('Processed in ', end - start, 'seconds')
