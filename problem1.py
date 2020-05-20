'''
Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.

Extras:
Add on to the previous program by asking the user for another number and printing out
that many copies of the previous message. (Hint: order of operations exists in Python)

Print out that many copies of the previous message on separate lines. (Hint: the string "\n is the same as pressing the ENTER button)
'''
name= input('Enter your name: ')
age= int(input('enter your age: '))
current_year=2020
remaining_years= 100-age
century_year= current_year + remaining_years
print(name,'will turn 100 years old in the year',century_year)
number_of_copies= int(input('Please enter the number of copies of meassage required: '))
a=1
while a<=number_of_copies:
    print(name,'will turn 100 years old in the year',century_year)
    a+=1

