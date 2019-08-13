import time

"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens. 
For example, 342 (three hundred and forty-two) 5 + 7 + 3 + 5 + 3  23 letters and 115 (one hundred and fifteen) contains 20 letters. 
The use of "and" when writing out numbers is in compliance with British usage.
"""

number_dict = {
    # 'and': 'and',
    1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five', 6: 'six', 7: 'seven', 8: 'eight', 9: 'nine', 10: 'ten', 11: 'eleven', 12: 'twelve', 
    13: 'thirteen', 14: 'fourteen', 15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen', 20: 'twenty', 30: 'thirty', 40: 'forty', 
    50: 'fifty', 60: 'sixty', 70: 'seventy', 80: 'eighty', 90: 'ninety', 1000: 'onethousand'
}

word_nums_dict = {}
    
# remove hyphens
def remove_hyphens_space():
    pass

# count word_num length
def count_number(word_num):
    return len(word_num)

# convert numbers into words (break apart word, call dictionary to get word, combine)
def make_nums_words(key):
    check_len = len( str(key) )
    if key in number_dict:
        # print(key, number_dict[key])
        return number_dict[key]

    elif check_len == 2:
        stringified_num = str(key)
        tens_col = stringified_num[0] + '0'
        tens_col = int(tens_col)
        tens_col = number_dict[tens_col]
        return tens_col + make_nums_words(int(stringified_num[1:]))

    elif check_len == 3:
        stringified_num = str(key)
        hundred_col = stringified_num[0] 
        hundred_col = int(hundred_col)
        hundred_col = number_dict[hundred_col]
        if  stringified_num[-2:] == "00":
            return hundred_col +'hundred'
        else: 
            return hundred_col +'hundredand' + make_nums_words(int(stringified_num[1:]))

def total_letters():
    sum = 0
    for i in range(1, 1001):
        word_num = make_nums_words(i)
        # print(i, word_num)
        sum += count_number(word_num)
    return sum

start = time.time()

print( total_letters() )

end = time.time()
print('Processed in ', end - start, 'seconds')