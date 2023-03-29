import random

# generate a random integer between 0 and 1 (inclusive) to simulate a coin toss
toss_num = random.randint(0, 1)

# print the result of the coin toss
if toss_num == 0:
    print('Tails')
elif toss_num == 1:
    print('Heads')
else:
    print('Unknown')  # in case the random integer generated is not 0 or 1
