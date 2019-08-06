import timeit
less_four_million = 31
# fib 32 = 5702887

def iter_fibo(idx):
    first = 1
    second = 2
    temp = first + second 
    fibs = [2]

    for i in range(3, idx+1):
        first = second 
        second = temp
        temp = first + second
        # if temp % 2 == 0:
        fibs.append(temp)
    return fibs[-1]

start = timeit.default_timer()

print( iter_fibo(less_four_million) )

stop = timeit.default_timer()
execution_time = stop - start
print("Program Executed in ", execution_time, "seconds")

