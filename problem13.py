'''
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
My name is Michele
Then I would see the string:

  Michele is name My
shown back to me.
'''
def rev(a):
    b=[]
    for i in a.split():
        b.append(i)
    c=b[::-1]
    for i in c:
        print(i,end=' ')


str=input('Enter a sentence: ')
rev(str)
