import random

# Intermediate Functions 1

def randint(min=0, max=100):
    if (min > max) or (max < 0):
        return False
    randInteger = round(random.random()*(max-min) + min)
    return randInteger

# print(round(random.random()*6))
print(randint(min=0, max=50))