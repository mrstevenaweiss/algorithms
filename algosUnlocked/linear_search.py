
# LINEAR SEARCH
# input:
# 1. an array, A
# 2. length of the array, n
# 3. the value to search, x

# output
# Either the index i when A[i] = x or 'not found'

# pseudo
# 1. For i = 0 to n:
    # A. If A[i] = x, then return the value of i as the output.
# 2. Return NOT-FOUND as the output.


def linear_search(A, x):
    length = len(A)
    i = 0

    for i in range(length):
        if A[i] == x:
            return i
    return 'Not found'

# SENTINEL SEARCH
# inputs / outputs the same as above

1. Save A[n] into last and then put x into A[n].
2. Set i to 0
3. While A[i] != x, do the following:
    A. Increment i.
4. Restore A[n] from last.
5. If i<n or A[n] == x, then return the value of i as the output.
6. Otherwise, return NOT-FOUND as the output.


def sentinel_search(A, element_to_search):
