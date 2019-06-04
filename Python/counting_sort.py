#!/usr/bin/python3

my_list= [4, 1, 5, 0, 1, 6, 5, 1, 5, 3]
constraint = 7

def count_keys_equal(numbers, constraint):
    length = len(numbers)
    equal = [0] * constraint
    
    for number in numbers:
        equal[number] += 1
    return equal
    
def count_keys_less(equal_numbers, constraint):
    less = [0] * constraint

    for index in range(1, len(equal_numbers)):
        less[index] = less[index - 1] + equal_numbers[index -1]
    print(less)
    return less

def rearrange(less_numbers, length_of_original_list, original_list):
    rearranged = [0] * length_of_original_list
    
    for i in range(length_of_original_list):
        to_sort = original_list[i]
        counted_sort_idx = less_numbers[to_sort]
        rearranged[counted_sort_idx] = to_sort
        less_numbers[to_sort] = less_numbers[to_sort] + 1 
    return rearranged
        
def counting_sort(any_list, constraint):
    equal = count_keys_equal(any_list, constraint)
    less = count_keys_less(equal, constraint)
    sorted_list = rearrange(less, len(any_list), any_list )
    
    return sorted_list

print(counting_sort(my_list, constraint))

