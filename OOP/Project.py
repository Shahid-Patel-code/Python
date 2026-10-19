# Design a class Mobile with the following requirements:

# The class should have a constructor to initialize:
# brand (name of the mobile)
# price (cost of the mobile)
# an empty list ratings to store user ratings

# Implement the following methods:
# 1)apply_discount(percent)
# Reduce the mobile price by the given discount percentage

#  2)compare_price(other_mobile)
# Compare the price of the current mobile with another mobile
# Display whether it is costlier, cheaper, or equal

# 3)add_rating(rating)
# Add a rating to the ratings

# 4) listavg_rating()
# Calculate and return the average rating of the mobile
# If no ratings are available, return 0

# 5) show()
# Display mobile details: brand, price, and ratings

#  Additional Requirement

#  Create at least two mobile objects and:

# Apply discount to one mobile
# Compare prices between them
# Add ratings
# Display average rating


import random
class Mobile:
    def __init__(self,name, price):
        self.brand= name
        self.price=price
        self.rating=[]
        self.ava=0
    def discount(self):
        self.discount=0
        num=random.randint(5,20)
        self.discount=self.price-self.price*num/100

    def compare(self,obj):
        print("------------------------------------")
        if self.price>obj.price:
            print(f"{obj.brand} has Low Market Price")
        elif self.price<obj.price:
            print(f"{self.price} has Low Market Price")
        else: 
            print("Both Have Same Price")
        print("------------------------------------")
    def rate(self):
        for i in range(1,6):
            rating=int(input(f"Enter {i} rating: "))
            self.rating.append(rating)

    def ava_rating(self):
        self.ava=sum(self.rating)/len(self.rating)

    def display(self):
        print("------------------------------------")

        print("Brand Name: ",self.brand)
        print("Market Price: ",self.price)
        print("Discounted Price: ",self.discount)
        print("Rating: ",self.rating)
        print("Avrage Rating: ", self.ava)

        print("------------------------------------")
name=input("Enter Brand of First Mobile: ")
price=int(input("Enter Price Of First Mobile: "))
obj=Mobile(name,price)
obj.discount()
obj.rate()
obj.ava_rating()
obj.display()
name=input("Enter Brand of Second Mobile: ")
price=int(input("Enter Price Of Second Mobile: "))
obj1=Mobile(name,price)
obj1=Mobile(name,price)
obj1.discount()
obj1.rate()
obj1.ava_rating()
obj1.display()

ans=input("Do You Wnat TO Compare Mobile Phones ")
if ans=="yes" or 'y':
    obj.compare(obj1)
elif ans=="no"or 'n':
    print("Thank You")
else:
    print("Enter Valid Answer y/n")


# create Complex class with instance veriable real and imaginary cerate a method as add_complex to 
# add 2 complex number Sub_complex to substaract 2 complex number 

class complex:
    def __init__(self):
        self.real=int(input("Enter Real number: "))
        self.complex=int(input("Enter complex number: "))
        self.op=input("Enter opretion(+ or -)")
        self.re=0
        self.img=0
    def opration(self,obj):
        if self.op=="+":
            self.re=self.real+obj.real
            self.img=self.complex+obj.complex
            print(f"Result={self.re} + {self.img}i")
        elif self.op=="-":
            self.re=self.real-obj.real
            self.img=self.complex-obj.complex
            print(f"Result={self.re} + {self.img}i")
obj=complex()
obj1=complex()
obj1.opration(obj)
