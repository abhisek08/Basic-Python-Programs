'''
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
 Hint: how does an even / odd number react differently when divided by 2?

Extras:

If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message.
'''
number= int(input('Enter a Number: '))
if number%4==0:
    print(number,'is a multiple of 4')
elif number%2==0:
    print(number,'is even')
else:
    print(number,'is odd')
num= int(input('Enter the checking number: '))
main_num= int(input('Enter a number to divide by the checking number: '))
if main_num%num==0:
    print(main_num,'is divisible by',num)
else:
    print(main_num,'is not divisible by',num)
