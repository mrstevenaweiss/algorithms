#problem
# for each index you want to find the product of every integer except the integer at that index.

#input
# list of integers

#output

#sudo

def get_products_of_all_ints_except_at_index(list_of_numbers):
    
    new_list = []
    
    # get initial number
    r = 1
    for x in range(1, len(list_of_numbers)):
        r *= list_of_numbers[x]
    new_list.append(r)
    
    
    
    
    
    print(new_list)

    # for number in list_of_numbers:
    #     print(number)

nums = [1, 7, 3, 4]

print(get_products_of_all_ints_except_at_index(nums))
