# Take a dictionary from user and seprate them by lenth words
take=[]
dictionary={}
for i in range(5):
    take1=input(f"Enter {i+1} element of list: ")
    take.append(take1)
for i in take:
   a= len(i)
   if a not in dictionary:
       dictionary[a]=[]
dictionary[a].append(i)
print(dictionary)

# find the number of charecter 
s=input("Enter a string: ")
dictionary={}
a=s.split()
for i in a:
    n=str.count(i)
    dictionary[i]=n
print(dictionary)

# write a program to swap given key value in dictionary
'''Dict={1:"one",2:"two",3:"three"}
Dict2={}
a=Dict.keys()  
b=Dict.values()
Dict2=(dict(zip(b,a)))
print(Dict2)
'''

# write a python program to take a dictionary from user
#  and take key value pair from use and remove from dictionary
'''
d={}
n=int(input("Enter number of keys: "))
for i in range(n):
    a=input("Enter a key: ")
    b=input("Enter a value: ")
    d[a]=b
print(d)
r=input("Enter a key you want to remove: ")
d.pop(r,"Key not Found")
print(d)        
'''
# write a program to sum all the value in given dictionary

d={}
n=int(input("Enter number of keys: "))
for i in range(n):
    a=input("Enter a key: ")
    b=int(input("Enter a value: "))
    d[a]=b
print(d)
a=d.values()
print(sum(a))