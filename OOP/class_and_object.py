
# class Goat:
#     '''Khalil Is A Goat Person'''
#     pass
# obj=Goat
# print(type(obj))
# print(obj)
# print(obj.__doc__)
# print(Goat)
# help(Goat)


# class with method and instance veriable
class Test:
    def f1(self):
        self.x=10
        print("value of x : ",self.x)
obj=Test()
obj.f1()

# class with method with self parameter 
'''class Test:
    def f1(self):
        print("Inside Test Class Fuction")
obj=Test()
obj.f1()

# write aprogram to create a class student with instans veriable name and roll number print details
# of student using instance method

class Student:
    def f1(self,n,r):
        self.roll=r
        self.name=n
        print("Your Name: ",self.name)
        print("Your Role_Number: ",self.roll)
num=int(input("Enter roll Number: "))
nav=input("Enter Name: ")
obj=Student()
obj.f1(nav,num)
# print(obj.__dict__)'''


# write aprogram to create a class employee with instance veriable name age and salary
# and create instance method display details to print details of 2 employees
'''
class Emp:
    def Input(self,Name,Age,Salry):
        self.name=Name
        self.age=Age
        self.salry=Salry
    def Display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Salry: ",self.salry)

num=int(input("Number of Employee: "))
for i in range(num):
    name=input("Enter your Name: ")
    age=int(input("Enter your Age: "))
    salry=int(input("Enter your Salary: "))
    obj=Emp()
    obj.Input(name,age,salry)
    obj.Display()'''

'''l=[]
class Emp:
    def Input(self,Name,Age,Salry):
        self.name=Name
        self.age=Age
        self.salry=Salry
    def Display(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Salry: ",self.salry)

num=int(input("Number of Employee: "))
for i in range(num):
    name=input("Enter your Name: ")
    age=int(input("Enter your Age: "))
    salry=int(input("Enter your Salary: "))
    obj=Emp()
    obj.Input(name,age,salry)
    obj.Display()
'''

# create a classs item having instance data member item name quantity and price it contain instance
# methods as to accepet the value of instance veriable to calculate net amount if total amount 
# is abovet 10 thousand then its 10% discount if amount is above 5000 and 5% discount else no 
# discount to display all detail with net amount  

class item:
    def data(self,Name,Price,Quantity,Net):
        self.name=Name
        self.price=Price
        self.quantity=Quantity
        self.diss=0
        self.Net=Net
        self.pr=self.price*10/100
    def Discount(self):
        if self.price>10000:
            self.diss=self.price-self.price*10/100
            self.pr=self.price*10/100
        elif 10000>self.price>5000:
            self.diss=self.price-self.price*5/100
            self.pr=self.price*5/100
        elif self.price<5000:
            print(f"You Net Amount is: {self.price}")
    def Display(self):
        print("-----Bill-----")
        print("Item Name: ",self.name)
        print("Item Price: ",self.Net)
        print("Item Quntity: ",self.quantity)
        print("Total Amount: ", self.price)
        print("Discounted price: ",self.pr)
        print("Net Price: ",self.diss)

name= input("Enter Name of Item: ")
net=int(input("Enter Price of Item: "))
quantity=int(input("Enter Quantity of Item: "))
price=(quantity*net)
obj=item()
obj.data(name,price,quantity,net)
obj.Discount()
obj.Display()


