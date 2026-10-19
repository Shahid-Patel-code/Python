# The Function Which Call itself.

# Find Faactorial Of n number using recursive function

'''def fact(n):
    if n==1:
        return 1
    else:
        return n*fact(n-1)

# num=int(input("Enter a Number: "))
print(fact(5))'''

# Assending Order
'''def number(n):
    if n==0:
        return 0
    print(n)
    number(n-1)
num=int(input("Enter a Number: "))
number(num)'''

# Decending order 
'''def number(n):
    if n==0:
        return 0
    number(n-1)
    print(n)
num=int(input("Enter a Number: "))
number(num)'''

# write a program to convert decimal number to binary number
'''def Bina(n):
    if n==0:
        return 0
    Bina(n//2)
    print(n%2)
n1=int(input("Enter a Number: "))
Bina(n1)'''

# write a program to print sum of digit of number using recursive function 
'''n1=0
def sum(n):
    global n1
    if (n)<1:
        return n
    n1=n1+n%10
    n2=n//10
    sum(n2)
    return n1
num=int(input("Enter a Nunber: "))
print(sum(num))
'''
# write a program to swap adjesent number in list using user define function 
'''def swap(L):
    for i in range(0,len(L)-1,2):
        L[i],L[i+1]=L[i+1],L[i]
    return L
l=[]
length=int(input("Enter a lenth of list: "))
if length%2!=0:
    print("Enter even length")
else:
        for i in range(length):
            num=int(input("Enter number: "))
            l.append(num)
print(swap(l))'''
