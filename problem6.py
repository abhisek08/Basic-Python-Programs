'''
Ask the user for a string and print out whether this string is a palindrome or not.
(A palindrome is a string that reads the same forwards and backwards.)
'''
string_= input('Enter a String: ')
a=[]
b=[]
for temp in string_:
    a.append(temp)
print(a)
b=a.copy()
b.reverse()
print(b)
num=0
count=0
county=0
while num<len(b):
    if a[num] in b[num]:
        count+=1
    else:
        county+=1
    num+=1
print(count)
print(len(a))
if count==len(a):
    print('the entered string is a palindrone.')
else:
    print('the entered string is not a palindrone.')
