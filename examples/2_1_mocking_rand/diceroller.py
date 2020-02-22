from random import randint

def roll_dice():
    result = randint(1, 10)
    if result > 7:
        return 'Success'
    return 'Failure'
