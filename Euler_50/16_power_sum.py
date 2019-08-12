import time

"""
2^15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 21000?
"""

print(2**15)

def power_sum():
    #calculate & stringify
    stringified = str(2**1000)
    # listify / split string into list
    items = list(stringified)
    # convert to ints and reduce
    test_list = sum( [int(i) for i in items] )
    print(test_list)

start = time.time()
power_sum()
end = time.time()
print('Processed in ', end - start, 'seconds')

######## Other approaches #######

# total = 0
# for i in test_list: 
#     print(i, total)
#     total += i
