'''
Write a program that takes a list of numbers (for example, a = [5, 10, 15, 20, 25]) and
makes a new list of only the first and last elements of the given list.
 For practice, write this code inside a function.
'''
def first_last(a):
    c=[a[0],a[-1]]
    print(c)
a=[]
n=int(input('enter the number of elements in the list'))
for i in range(0,n):
    b=int(input())
    a.append(b)
first_last(a)