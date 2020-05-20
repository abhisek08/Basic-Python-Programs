'''
Write a password generator in Python.
Be creative with how you generate passwords - strong passwords have a mix of lowercase letters, uppercase letters, numbers, and symbols.
The passwords should be random, generating a new password every time the user asks for a new password.
Include your run-time code in a main method.

Extra:

Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
'''
import random
s='abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*.'
reqd_len=8
lst=['good','bad','hello','blast','best']
if input('strong or weak password: ')=='strong':
    c=random.sample(s,reqd_len)
    d=''
    for i in c:
        d=d+i
    print(d)
else:
    c = random.sample(s,2)+ random.sample(lst,1)
    d = ''
    for i in c:
        d = d + i
    print(d)