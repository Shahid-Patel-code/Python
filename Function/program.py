# write a program to make a clculater using user define functions
'''def f1(n1,n2):
    print(f"{n1}+{n2}={n1+n2}")
def f2(n1,n2):
    print(f"{n1}-{n2}={n1-n2}")
def f3(n1,n2):
    print(f"{n1}*{n2}={n1*n2}")
def f4(n1,n2):
    print(f"{n1}/{n2}={n1/n2}")
num=int(input("Enter a number: "))
op=input("Enter Oprator(+ - * /): ")
num2=int(input("Enter a number: "))
if op=="+":
    f1(num,num2)
elif op=="-":
    f2(num,num2)
elif op=="*":
    f3(num,num2)
elif op=="/":
    if num2>0:
        f4(num,num2)
    else:
        print("∞")
'''

# write a program to access a string and count number of upper and lower case latters using user 
# define functions with parameter and return value
'''upper=0
lower=0
def case(n):
    if n.isupper():
        return 1
    elif n.islower():
        return 0

Str=input("Enter A string: ")
for i in Str: 
    result=case(i)
    if result==1:
        upper+=1
    elif result==0:
        lower+=1
print("Upper case letter in string: ",upper)
print("lower case letter in string: ",lower)
''' 
def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

# num=int(input("Enter a Number: "))
fact(5)

