

# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import math

def solution(N):
    l = [None] * N
    if len(l) % 2 == 1:
        num = math.ceil( len(l)/2 )
        mid_point = num-1
        l[mid_point] = 0
  
        subtractor = -1
        for i in reversed(range(mid_point)):
            l[i] = subtractor
            subtractor = subtractor-1
        
        adder = 1
        for x in range(mid_point+1, len(l)):
            l[x] = adder
            adder = adder+1

    else:
        num = math.ceil( len(l)/2 )
        even_mid_point = num

        subtractor = -1
        for i in reversed(range(even_mid_point)):
            l[i] = subtractor
            subtractor = subtractor-1

        adder = 1
        for x in range(even_mid_point, len(l)):
            l[x] = adder
            adder = adder+1
    
    return l
    pass


