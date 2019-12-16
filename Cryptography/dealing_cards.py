
suits = ["Clubs", "Hearts", "Spades", "Diamonds"]

for i in range(1, 53):
    
    if i <= 13: 
        suit = suits[0]    
    elif i > 13 and i <= 26: 
        suit = suits[1]
    elif i > 26 and i <= 39: 
        suit = suits[2]
    elif i > 39: 
        suit = suits[3]
    print(suit, 'bitwise', i)