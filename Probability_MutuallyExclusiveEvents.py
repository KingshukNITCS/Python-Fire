# Mutually Exclusive Events
# Mutually exclusive events are events that cannot occur at the same time.

import random

def roll_dice():
    return random.randint(1, 6)

def flip_coin():
    return random.choice(['heads', 'tails'])

dice_roll = roll_dice()
if dice_roll == 3:
    print("Dice Roll:", dice_roll)
    print("Coin Flip: Not Possible")
else:
    coin_flip = flip_coin()
    print("Dice Roll:", dice_roll)
    print("Coin Flip:", coin_flip)
'''
Dice Roll: 3
Coin Flip: Not Possible
'''
