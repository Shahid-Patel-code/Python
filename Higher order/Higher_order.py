# write a program to sort the list of dictionary on basis of price 
d=[{"item":"pen", "price":50},
   {"item":"pensil", "price":10},
   {"item":"notebook", "price":20},
   {"item":"Eraser", "price":30},
   {"item":"Shrpner", "price":4}]

d1=filter(lambda x: x["price"]>10,d)
print(sorted(d1,key=lambda x:x["price"]))

# Use of lambda
# write a program to check number is divisible by 3 or not using lamda function
'''f1=lambda x: print(f"{x} is divisible by 3 ") if x%3==0 else print(f"{x} is not divisible by 3 ")
num=int(input("Enter a number: "))
f1(num)'''

# write a program to check number is positive or not using lamda function 
'''f2=lambda x: print(f"{x} is positive Number ") if x>0 else print(f"{x} is negative number")
num=int(input("Enter a number: "))
f2(num)'''

# write a program to take tupple as a parameter and find min and max value using lambda function
'''f3=lambda * n: print(f"""Maximum value: {max(n)} 
Minimum value: {min(n)} """)
f3(1,2,3,4,5,6,7,8,99)
'''
# write a program to sort the dictionary 
'''d2={'abc':1,'pqrs':2}
print(sorted(d2,key=len))
'''

# write a program to sort the dictionary  
'''def f1(d):
    a=sorted(d,key=lambda x: d[x])
    b=sorted(d.values())
    print(dict(zip(a,b)))
d1={"r":22,"y":12}
f1(d1)
'''
# write a program to take list of dictinry from user and sort accrding keys

# write a program to sort a list using lambda function by even and odd order
'''l=[2,1,5,8,3]
print(sorted(l,key=lambda x: (x%2,x)))'''

# write a program to sort given list based on second digit 
'''l=[23,45,81,27]
print(sorted(l,key=lambda x: x%10))'''

# write a program to sort list such taht odd number first sort odd number in desending order 
#sort even number in assending order using lambda function
'''l=[8,7,5,4,2,1]
print(sorted(l,key=lambda x: (x%2==0,-x if x%2 else x)))'''

# Self Program
# anonymus function: A function without name

# function with no parameter and no return type
f1=lambda : print("Python")
f1()

# function with no parameter and return type
f2=lambda: "Python"
print(f2())

# function with parameter and no return type
f3=lambda x: print(x)
f3("Python") 

# function with parameter and return type
f4=lambda x: x*5
print(f4(5))

# function with veriable parameter
f5=lambda *args: print("Sum of argument: ", sum(args))
f5(5,10,4,3,6)

# function with keyword argument
f6=lambda **args: print("Sum of argument: ", sum(args.values()))
f6(a=7,b=3,c=6)

