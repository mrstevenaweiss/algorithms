# Write a function that takes a list of characters and reverses the letters in place.

def reverse_words(message):
    start = 0
    end = len(message)-1

    while start < end:

        message[end], message[start] = message[start], message[end]
        start += 1
        end -= 1

    return message
