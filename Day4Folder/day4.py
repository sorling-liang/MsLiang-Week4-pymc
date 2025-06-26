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
tries = 1
while guess != hidden:
    print("wrong! try again!")
    tries = tries + 1
    guess = input( riddle ) # ask again
else:
    print("you are correct! and you got it after " + str(tries) + " tries.")

########################################################################
# Additional exercises: