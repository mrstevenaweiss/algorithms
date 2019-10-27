
import timeit

start = timeit.default_timer()
million = 10**7
def a_million():
    nums = 0
    for i in range(million+1):
        nums = nums + i
    return 'a sum', nums
a_million()
stop = timeit.default_timer()
execution_time = stop - start
print("Program Executed in ", execution_time, "seconds")

start = timeit.default_timer()
def check_sum(N):
    return N*(N+1) / 2 
check_sum(million)
stop = timeit.default_timer()
execution_time = stop - start
print("Program Executed in ", execution_time, "seconds")
