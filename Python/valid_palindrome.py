#!/usr/bin/python3


def dealer(letters, subtract ):

    i = 0
    letter_even = 0
    letter_odd = 1

    while i < (len(letters)-subtract)/2:

        if letters[letter_even] == letters[letter_odd]:
            print(i, letters[letter_even], letters[letter_odd])

            i += 1
            letter_even += 2
            letter_odd += 2
        else:
            return False

    return True

def checker(string):

    letters = sorted(list(string))
    print(letters)

    if len(letters) % 2 == 1:
        x = -1
        return dealer(letters, x)

    else:
        x = 0
        return dealer(letters, x)



word = "cici"

print(checker( word ))

def has_palindrome_permutation(the_string):
    # Track characters we've seen an odd number of times
    unpaired_characters = set()

    for char in the_string:
        if char in unpaired_characters:
            unpaired_characters.remove(char)
        else:
            unpaired_characters.add(char)

    # The string has a palindrome permutation if it
    # has one or zero characters without a pair
    return len(unpaired_characters) <= 1
