
import time
'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''
def least_common_multiple():
    """You need to know primes and the # of powers < N"""
    # Rethinking an earlier attempt at Prime factorization 
    first = 2**4
    second = 3**2
    return first*second*5*7*11*13*17*19
  

start = time.time()
print( least_common_multiple() )
end = time.time()
print('Processed in ', end - start, 'seconds')


# 1st approach
# # # # a_list[0] = number % 2 != 0
# # # #     a_list[1] = number % 3 != 0
# # # #     a_list[2] = number % 4 != 0
# # # #     a_list[3] = number % 5 != 0
# # # #     a_list[4] = number % 6 != 0
# # # #     a_list[5] = number % 7 != 0
# # # #     a_list[6] = number % 8 != 0
# # # #     a_list[7] = number % 9 != 0
# # # #     a_list[8] = number % 10 != 0
# # # #     a_list[9] = number % 11 != 0
# # # #     a_list[10] = number % 12 != 0
# # # #     a_list[11] = number % 13 != 0
# # # #     a_list[12] = number % 14 != 0
# # # #     a_list[13] = number % 15 != 0
# # # #     a_list[14] = number % 16 != 0
# # # #     a_list[15] = number % 17 != 0
# # # #     a_list[16] = number % 18 != 0
# # # #     a_list[17] = number % 19 != 0
# # # #     a_list[18] = number % 20 != 0
# # # #     lister = True in a_list
# # # #     number += 2
    
# 2nd approach
# # #   if number % 1 == 0:
# # #     print('fourth loop')
# # #     adder += 1
# # #     if number % 2 == 0:
# # #       adder += 2
# # #       if number % 3 == 0:
# # #         adder += 3
# # #         if number % 4 == 0:
# # #             adder += 4
# # #             if number % 5 == 0:
# # #                 print(number)
# # #                 # adder += 5