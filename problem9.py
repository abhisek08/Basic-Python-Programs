'''
Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.
(Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out.
'''
def gues(a,b):
    if a == b:
        print("exactly right")
    elif b < a:
        print('too low')
    else:
        print('too high')
import random
a=random.randint(1,9)
b=int(input('Guess a number: '))
gues(a,b)
c=1
while input('Do you want to exit? ')!='exit':
    b = int(input('Guess a number: '))
    gues(a,b)
    c+=1
print('the user took {} guesses'.format(c))