import time
"""
A permutation is an ordered arrangement of objects. 
For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. 
If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. 
The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?

Pseudo:
0. Heap's Algo
1. Change #'s to strings/ints
2. Sort

"""


# numbers = [120, 12, 201, 210, 21, 102]
inputs = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# inputs = [0, 1, 2]

def stringify_nums(nums):
    stringify = ''
    for i in nums:
        stringify += str(i)
    return stringify

#Prints the array 
full = []
def printArr(a, n): 
    listed = []  
    for i in range(n): 
        # print(a[i],end="") 
        listed.append(a[i])
    # print() 
    num = stringify_nums(listed)
    # print('nummer', num)
    full.append(num)

# Generating permutation using Heap Algorithm 
def heapPermutation(a, size, n): 
    # if size becomes 1 then prints the obtained 
    # permutation 
    if (size == 1): 
        printArr(a, n) 
        return
  
    for i in range(size): 
        heapPermutation(a,size-1,n); 
        # if size is odd, swap first and last 
        # element 
        # else If size is even, swap ith and last element 
        if size&1: 
            a[0], a[size-1] = a[size-1],a[0] 
        else: 
            a[i], a[size-1] = a[size-1],a[i] 

# Convert permuted numbers back into integer form
def intify_nums(nums):
    intify = []
    for i in nums:
        intify.append(int(i))
    return intify

# Driver code 
def get_all_perm(inputs):
    n = len(inputs) 
    heapPermutation(inputs, n, n) 
    # print('full', full)
    ints = intify_nums(full)
    # print('ints', ints)
    ints = sorted(ints)
    print(ints[999999])

start = time.time()
get_all_perm(inputs)
end = time.time()
print('Processed in ', end - start, 'seconds')