'''
 You, the user, will have in your head a number between 0 and 100.
 The program will guess a number, and you, the user, will say whether it is too high, too low, or your number.

At the end of this exchange, your program should print out how many guesses it took to get your number.

As the writer of this program, you will have to choose how your program will strategically guess.
 A naive strategy can be to simply start the guessing at 1, and keep going (2, 3, 4, etc.) until you hit the number.
 But that’s not an optimal guessing strategy. An alternate strategy might be to guess 50 (right in the middle of the range),
  and then increase / decrease by 1 as needed. After you’ve written the program, try to find the optimal strategy!
 (We’ll talk about what is the optimal one next week with the solution.)
'''
import random
import sys
a=random.randint(0,1)
print('the generated number is',a)
b=input('Is it too high,too low or your number: ')
if b=='your number':
    sys.exit()
else:
    count=1
    while b!='your number':
        a = random.randint(0, 3)
        print('the generated number is', a)
        b = input('Is it too high,too low or your number: ')
        count+=1
print('The computer took {} guesses'.format(count))