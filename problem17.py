'''
Write a function that takes an ordered list of numbers (a list where the elements are in order from smallest to largest) and another number.
The function decides whether or not the given number is inside the list and returns (then prints) an appropriate boolean.

Extras:

Use binary search.
'''
def search(lst,a):
    lst.sort()
    if a in lst:
        print(True)
    else:
        print(False)

lst=[23,21,45,34,87,645,32,54]
a=int(input('enter the number to be found: '))
search(lst,a)