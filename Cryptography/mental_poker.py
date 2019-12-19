## Mental Poker

import random, math 

bitwise_cards = {}

# Create a bitwise hash
suits = ["Clubs", "Hearts", "Spades", "Diamonds"]
cards = [None, "Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", None]
card = 1

for i in range(1, 53):
    if i <= 13: 
        suit = suits[0]    
    elif i > 13 and i <= 26: 
        suit = suits[1]
    elif i > 26 and i <= 39: 
        suit = suits[2]
    elif i > 39: 
        suit = suits[3]
    if card == 14:
        card = 1 
    # print(suit, cards[card], 'bitwise=', i)
    bitwise_cards[i] = cards[card] + suit
    card += 1
# print(bitwise_cards)

# Dealing cards with Keys
# Key == "MY" key (a huge digit)
bitwise_random = random.randint(1, 52)
print(bitwise_random, bitwise_cards[bitwise_random])

# Stage 1: bitwise_random^K % P 
# P is some large number or a prime number
print( math.pow(bitwise_random, 2) % P ) 

# Stage 2: ( bitwise_random^K )^J % P  == ( bitwise_random^J )^K % P
# Stage 3: (( bitwise_random^J )^K)^-1K % P == ( bitwise_random^J ) % P
# Stage 4: ( bitwise_random^J )^-1J % P == bitwise_random % P


# Repeated Squaring // Raising large problems efficiently
# Q^11 = Q^1 * (Q^5)^2 

#  it is not the inverse in Q, but the inverse modulo p-1.That is, take a number i such that ki = 1 modulo p-1
# The Fermat little theorem say that a^(p-1) = 1 modulo p
# Then (q^k)^i = q^(ki) = q modulo p
# For example if p=23 and k=7, then p-1=22, moreover 19*7 = 6*22+1 = 1 modulo 22.
# So for any integer x we have (x^7)^19 = x modulo 23
# For example 15^7 = 170859375 = 11 modulo 23
# and 11^19 = 61159090448414546291 = 15 modulo 23
# (of course you should reduce the power modulo p directly)