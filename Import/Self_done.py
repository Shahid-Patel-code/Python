import string
# print(string.ascii_letters)
# print(string.ascii_uppercase)
# print(string.ascii_lowercase)
# print(string.whitespace)
# print(string.hexdigits)
# print(string.punctuation)

'''str=input("Enter a string: ")
for i in str:
    if i in string.ascii_lowercase:
        print(f"{i} is lowerletter")
    if i in string.ascii_uppercase:
        print(f"{i} is uppercase")
    if i in string.whitespace:
        print(f"{i} is Whitespace")
    if i in string.punctuation:
        print(f"{i} is punctuation")
    if i in string.digits:
        print(f"{i} is digit")'''

"""import random
a= string.ascii_lowercase
b= string.ascii_uppercase
c= string.punctuation
d= string.digits
uni=a+b+c+d
print(random.choices(uni, k=4))"""






# Randon Module
# Write a Python program to generate a secure password of a user-defined length.                                                                                         
# The password must contain at least one uppercase letter, one lowercase letter, 
# one digit, and one special character.             
# The remaining characters should be selected randomly, and print  final password.
'''import random as r
def f1():
    global uni
    a=(string.ascii_lowercase)
    b=(string.ascii_uppercase)
    c=(string.digits)
    d=(string.punctuation)
    uni=a+b+c+d
    return uni

num=int(input("Enter length of password: "))
unii=f1()
while True:
    if num <3:
        print("Enter number greater than 4")
        break
    else:
        Pass=(r.choices(unii,k=num))
        digi=False
        upper=False
        lower= False
        punc=False
        for i in Pass:
            if i in string.digits:
                digi=True
            if i in string.ascii_uppercase:
                upper=True
            if i in string.ascii_lowercase:
                lower= True
            if i in string.punctuation:
                punc= True
        if digi and upper and lower and punc is True:
            print(Pass)
            break
        else:
            unii= f1()'''
