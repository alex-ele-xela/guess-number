###############################
# file guess.py               #
# authors Nanak Tattyrek      #
#         alex-ele-xela       #
# version 1.0                 #
###############################

import random


def getnum(msg=''):
    '''Takes input with printed message (msg)
    Successfully returns a valid integer number and handles ValueError'''

    try:
        x = int(input(msg))
    except ValueError:
        print("Please enter an integer number. Try again")
        return getnum(msg)
    return x


try:
    while True:
        #Accepts the low and high, while making sure that low < high

        low = getnum("Enter the lower bound for the game - ")
        high = getnum("Enter the upper bound for the game - ")

        if low < high:
            break
        else:
            print("Upper Bound must be greater than Lower Bound. Try Again\n")
except KeyboardInterrupt:
    print("\n^C detected, terminating...")
    exit(0)


guesslimit = 5

print(f"\nGuess the number between {low} and {high}")
print(f"You have {guesslimit} guesses to get the right number")

number = random.randint(low, high)

try:
    while guesslimit:
        '''The loop ends only if there are no more tries left (guesslimit = 0)
        Or if the guess is correct'''
        
        guess = getnum("\nWhat's your guess? ")

        if guess < low or guess > high:
            print("Value out of range ({0} - {1})".format(low, high))

        if guess < number:
            print("Your guess was too low")
        elif guess > number:
            print("Your guess was too high")
        else:
            break

        guesslimit -= 1

except KeyboardInterrupt:
    print("\n^C detected, terminating...")
    exit(0)

except EOFError:
    print("\n^D detected, terminating...")
    exit(0)

if guess == number:
    print(f"\n{guess} is the Correct Answer!!\nGreat, you guessed the number in {6-guesslimit} tries")
else:
    print(f"\nNo, I was thinking of the number {number}")
