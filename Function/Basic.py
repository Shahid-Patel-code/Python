# making and calling a function 
'''def a():        # making Function
    print("hello")
a()             # Calling Function
'''

# function with no argument and no return value
'''def f1():        
    print(" function with no argument and no return value")
    print("hello")
f1()  
'''

# function with no argument and return value
'''def f2():
    print("function with no argument and no return value")
    return "Hello"         # return Value 
result=f2
print(result)
'''

# function with argument and no return value
'''def f3(name):           # Argument given
    print(" function with  argument and no return value")
    print(f"hello {name}")
n=input("Enter Your Name: ")
f3(n)                   # Argument Given to Function
'''

#  function with argument and return value
'''def f4(name):           # Argument given
    print(" function with  argument and no return value")
    return f"hello {name}"  # return Stetment
n=input("Enter Your Name: ")
f4(n)             
'''
# Function with default value
'''def f5(x=20):
    print("Function with default value")
    print("x: ",x)
f5()
f5(30)'''



def sk(n):
    print("Hi")
sk(10)
