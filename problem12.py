'''
Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

Extras:

Write two different functions to do this - one using a loop and constructing a list, and another using sets.
Go back and do Exercise 5 using sets, and write the solution for that in a different function.
'''
def no_duplicate(lst):
    lst2=set(lst)
    print(lst2)


n=int(input('enter the desired number of elements: '))
lst=[]
for i in range(0,n):
    ele=int(input())
    lst.append(ele)
no_duplicate(lst)
