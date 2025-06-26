# Write all your codes for Day 4 here.
# COMMENT out the previous task before going on to the next task
print("hello from day4")

import random
for count in range(10):
    diceValue = random.randint(1, 9999)
    print(diceValue)

########################################################################
# Task 1:



########################################################################
# Task 2:

riddle = "what do you call a deer with no eyes?"
hidden = "no idea"
guess = input( riddle )
while guess != hidden:
    print("wrong! try again!")
guess = input( riddle )
if guess == hidden:
    print("you are correct!")
else:
    print("wrong! try again!")

########################################################################
# Additional exercises: