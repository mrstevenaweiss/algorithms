import time
import math
import abundants_23

"""
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number. 
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, 
the smallest number that can be written as the sum of two abundant numbers is 24. 
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers. 
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest 
number that cannot be expressed as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
"""

# abundants = abundants_23.abundants
# non_abundants = abundants_23.non_abundants
# non_abundants = []
abundants = []

def getFactors(n):
    """ Get factors less the N"""
    sum = 0
    i = 1
    while i <= (math.sqrt(n)):
        if n%i == 0:
            if n/i == i:
                sum += i
            else: 
                sum += i
                sum += (n / i)
        i += 1
    sum = sum - n
    return int(sum)


# there is an error in this logic...need to change Get_Div_Sum
def create_abundants_non_abuns(n):
    """Create a list of abundant and non-abundant numbers; Memoized in abundants_23 file"""
    for i in range(1, n+1):
        get_div_sum = getFactors(i)
        if get_div_sum > i:
            abundants.append(i)
    del abundants[0]
    # print('abundants', abundants)
create_abundants_non_abuns(28123)

sums = [0]*28124
for x in range (0, len(abundants)):
    for y in range (x, len(abundants)):
            sumOf2AbundantNums = abundants[x] + abundants[y]
            if (sumOf2AbundantNums<= 28123):
                if (sums[sumOf2AbundantNums] == 0):
                    sums[sumOf2AbundantNums] = sumOf2AbundantNums

total = 0
for x in range (1,len(sums)):
    if (sums[x] == 0):
        total +=x

print('\n', total)

# double_abuns = {}
# def all_abuns_multiples():
#     """Create a dict of all the possible factors below 28123"""
#     for num in abundants:
#         for next_num in abundants:
#             double = num + next_num
#             if double <= 28123 and double not in double_abuns:
#                 double_abuns[double] = 1
#             else: 
#                 continue
#     # print('double abuns', double_abuns)

# double_double_abuns = []
# def convert_double_to_list():
#     """Convert the dictionary keys into a list to prep for list comp"""
#     for abuns in double_abuns:
#         double_double_abuns.append(abuns)
#     print(double_double_abuns)

# print(sum(double_double_abuns))
# start = time.time()
# all_abuns_multiples()
# convert_double_to_list()
# print(sum(double_double_abuns))
# """ Creating the correct 'intersection' then taking the sum """
# final = [x for x in non_abundants if x not in double_double_abuns]
# print(final)
# print('final', sum(final))

# end = time.time()
# print('Processed in ', end - start, 'seconds')