# You want to build a word cloud,
# an infographic where the size of a word corresponds
# to how often it appears in the body of text.

#!/usr/bin/python3
import re


def strip_split(words):
    out = re.sub(r'[^\w\s]','', words)
    split_sent = out.split()

    return split_sent

def word_dictionary(words):
        words_to_counts = {}

    # 1. Strip/split words
    clean_words = strip_split(words)

    # 2. Count words into a dictionary
    for word in clean_words:
        if word in words_to_counts:
            words_to_counts[word] += 1
        else:
            words_to_counts[word] = 1
    #
    # 3. Handle capital letters
    # handle later...

    return words_to_counts


phrase = 'Add milk and eggs, then add flour and sugar.'

print(word_dictionary(phrase))
