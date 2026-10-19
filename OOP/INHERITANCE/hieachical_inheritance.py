# Write a Python program to design and implement a Smart E-Commerce Fraud and 
# Reward System using Object-Oriented Programming concepts, Hierarchical Inheritance, and Data Structures.

# Create a base class User and derive the classes Customer, Seller.
# 1.Base Class: User
# Create a class User containing the following data members:
#                 user_id
#                 username
#                 email
#                 login_attempts
#                 account_status
# Methods
# login(password) : Allow maximum 3 login attempts.
#                   If login attempts exceed the limit, the account should become blocked.
# display_info() :user ID
#                 username
#                 email
#                 account status

# 2. Derived Class: Customer
# Create a class Customer inherited from User.
#                 Data Members
#                         wallet_balance
#                         cart
#                         reward_points
#                         order_history
#                         coupon_codes

# Use:
# list : to store cart items ,order history
# set : to store unique coupon codes.

# Methods
# 1)add_to_cart(product, price, quantity) :Add products into cart.
#                 Conditions 
#                         Product quantity cannot exceed 5 units.
#                         If the product already exists in cart, update quantity instead of adding duplicate entry(use list of dictionaries).
# 2)view_cart() :Display all products available in cart.

# 3)calculate_bill() Calculate: 
#                 subtotal
#                 GST
#                 delivery charges
#                 discount
#                 final amount
#                 Billing Rules
#                 GST
# Billing Rules
# 1) GST=18%×Subtotal

# 2) Delivery Charges
#             Bill Amount	Delivery Charges
#             Above ₹3000	free
#             Below ₹3000	150
# 3)Coupon Rules
#                 Coupon Code	Discount
#                 SAVE10	10%
#                 SUPER20	20%
# Coupon codes cannot be reused.


# 4)place_order()
# Reward Point Rules
#                 For every: 100Rs spent
#                 customer earns: 10 reward points
# Conditions
#                 user account must be active
#                 wallet balance should be sufficient
#                 cart should not be empty

# After successful order:
#                 deduct wallet balance
#                 generate reward points
#                 move order to order history
#                 clear cart

# 3. Derived Class: Seller

# Create a class Seller inherited from User.

# Data Members
#                 inventory
#                 sales_history
#                 seller_rating
#                 returned_orders
# Use:
# dictionary :to store inventory.
# list :to store sales history.

# Methods
# 1)add_product(product, stock, price) :Add product into inventory 
#                                       use separate dictionary for each product
#                                     Conditions
#                                          If product already exists, update stock quantity.
#                                          Negative stock values are not allowed.
# 2)sell_product(product, quantity) :Sell product from inventory.
#                                     Conditions
#                                            sufficient stock must be available
#                                     After selling:
#                                             reduce stock
#                                             update sales history(add in tuple)

# 3)return_order(product, quantity)
#                         Conditions
#                         returned quantity cannot exceed sold quantity
#                         Returned stock should be added back into inventory.

# 4)calculate_profit() Calculate seller profit using profit margins:

#                                 Product Type	Profit Margin
#                                 Electronics	       25%
#                                 Clothing	       40%
#                                 Others	           30%
# 5)check_low_stock() Display products where: 
#                     stock < 5



# sample input
# ------------- CUSTOMER DETAILS -------------

# Enter Customer ID: C101
# Enter Customer Name: Rahul
# Enter Email: rahul@gmail.com
# Enter Wallet Balance: 70000

# ------------- CUSTOMER LOGIN -------------

# Enter Password: 1234

# ------------- ADD PRODUCTS TO CART -------------

# Enter Product Name: Laptop
# Enter Price: 45000
# Enter Quantity: 1

# Enter Product Name: Mouse
# Enter Price: 1000
# Enter Quantity: 2

# Enter Product Name: Keyboard
# Enter Price: 3000
# Enter Quantity: 1

# Enter Coupon Code: SAVE10

# ------------- SELLER DETAILS -------------

# Enter Seller ID: S201
# Enter Seller Name: TechStore
# Enter Seller Email: tech@gmail.com

# ------------- ADD INVENTORY -------------

# Enter Product: Laptop
# Enter Stock: 10
# Enter Price: 45000

# Enter Product: Mouse
# Enter Stock: 20
# Enter Price: 1000

# Enter Product: Keyboard
# Enter Stock: 4
# Enter Price: 3000

# ------------- SELL PRODUCT -------------

# Enter Product To Sell: Laptop
# Enter Quantity: 1
# ------------------------------------------------------------------------------------------------------------

# sample output
# ------------- CUSTOMER INFORMATION -------------

# User ID: C101
# Username: Rahul
# Email: rahul@gmail.com
# Account Status: Active

# Login Successful

# ------------- CART OPERATIONS -------------

# Laptop added to cart
# Mouse added to cart
# Keyboard added to cart

# ------------- VIEW CART -------------

# Laptop Price: 45000 Quantity: 1
# Mouse Price: 1000 Quantity: 2
# Keyboard Price: 3000 Quantity: 1

# ------------- BILL DETAILS -------------

# Subtotal: 50000

# GST: 9000.0

# Delivery Charges: 0

# Discount: 5000.0

# Final Amount: 54000.0

# ------------- ORDER STATUS -------------

# Order Placed Successfully

# Remaining Wallet Balance: 16000.0

# Reward Points Earned: 5400

# ------------- SELLER OPERATIONS -------------

# Laptop added successfully
# Mouse added successfully
# Keyboard added successfully

# Laptop sold successfully

# Laptop returned successfully

# Seller Profit: 11250.0

# ------------- LOW STOCK PRODUCTS -------------

# Keyboard
import random as rm
import string as str
import time 
import datetime as dt
class user:
    
    def __init__(self):
      self.user_id="".join(rm.choices(str.digits+str.ascii_uppercase,k=4))
      self.username=input("Enter Your User name: ")
      self.mail=input("Enter Your Email: ")
      self.Pass=input("Enter Your Password: ")
      self.login_attempt=3
      self.Account_status=False
      self.view=False
      self.bag=False
      self.total=False
      self.place_order=False
      self.add=False
      self.sell=False
      self.returned=False
      print("Account Created Succesfully")
        
    def login(self): 
       print("-----------Class User-----------")
       print("-------------------------------------")
       while self.login_attempt>0:
            Pass=input("Enter Your Password: ")
            if Pass!=self.Pass:
                print("Wrong Password! ")
                self.login_attempt-=1
                if self.login_attempt==0:
                    print("Your Account Is Blocked For")
                    i=10
                    while i>0:
                        dt.datetime.now()
                        print(f"{i} ",end="\r")
                        time.sleep(1)
                        i-=1
                        self.login_attempt=3
            else: 
                print("Login succesfull")
                self.Account_status=True
                self.view=True
                self.bag=True
                self.bill=True
                self.place_order=True
                self.add=True
                self.sell=True
                self.returned=True
                break
    print("-------------------------------------")
        
    def Display(self):
        print("-------------------------------------")
        if self.Account_status==True:
          print(f"""
        ----->USER DETAILS<-------
        User Id-->{self.user_id}
        User Name--> {self.username}
        Email-->{self.mail}
        Account Status--> Online""")
        print("-------------------------------------")

class customer(user):
    
    def __init__(self):
        super().__init__()
        self.wallet=50000
        self.cart=[]
        self.reword=0
        self.order_history=[]
        self.coupon=["Goat10", "Goat20"]
    def Cart(self):
        if self.bag==True:
            print("-----------Class Cusomer-----------")
            print("-------->Cart<---------")

            for i in range (3):
                name = input("Enter Product Name: ")
                quan = int(input("Enter Quantity: "))
                price = int(input("Enter Price: "))
                net = quan * price
                if name not in self.cart:
                    self.cart.append({
                    name: [quan, net]})
                elif name in self.cart:
                    self.cart.append({
                name: [quan, net]})
        print("-------------------------------------")
    def view(self):
        print("-------->View<---------")
        print("-------------------------------------")
        for i in self.cart:
            print(i)
        print("-------------------------------------")
    def Bill(self):
        if self.total==True:
            print("-------->Bill<---------")
            print("-------------------------------------")
            self.bill=0
            self.net=0
            for i in self.cart:
                for key in i:
                    self.bill+=i[key][1]
            self.net=self.bill+self.bill*18/100
            if self.net<3000:
                self.net+=150
            ans=input("Do you Want to apply Coupon Yes/No: ")
            if (ans=="Yes")or("yes"):
                num=1
                for i in self.coupon:
                    print(f"{num}.{i}")
                    num+=1
                code=input("Enter Coupon Code: ")
                if code in self.coupon:
                    save=int(code[-2:])
                    self.net-=self.net*save/100
                else: 
                    print("Ye To Hum Pe Heyi No")
            elif (ans=="No")or("no"):
                print("Thanks For Not Taking Our Profit")
            print("-------------------------------------")
    def Place_order(self):
        if self.Place_order==True:
            print("-------->Place_Order<---------")
            print("-------------------------------------")
            if self.Account_status==True and self.net<self.wallet and len(self.cart)>0:
                self.reword=self.net/100
                self.wallet-=self.net
                self.order_history.extend(self.cart)
                self.cart.clear()
                print("Order Placed Succesfully")
        print("-------------------------------------")
print()

class seller(user):
    
    def __init__(self):
        super().__init__()
        self.inventory={}
        self.sales_history=[]
        self.returned_order={}
   
    def add_product(self):
        print("-----------Class Seller-----------")
        print("-------->Add_Product<---------")
        print("-------------------------------------")
        name = input("Enter Product Name: ")
        quan = int(input("Enter Quantity: "))
        price = int(input("Enter Price: "))
        self.inventory[name]=[quan,price]
        print("Poduct Added To Inventory")
        print("-------------------------------------")

    def sell_prduct(self):
        print("-------->Sell_Product<---------")
        print("-------------------------------------")
        name = input("Enter Product Name: ")
        quan = int(input("Enter Quantity: "))
        if name in self.inventory:
            if self.inventory[name][0]>=quan:
                print("Product Sell Sucessfully ")
                self.inventory[name][0]-=quan
                self.sales_history.append({name:(quan)})
            else:
                print(f"The {name} is lower Than Required Quantity ")
        else:
            print("No Product In Inventory")
        print("-------------------------------------")
    
    def return_product(self):
        print("-------->return_product<---------")
        print("-------------------------------------")
        name = input("Enter Product Name: ")
        quan = int(input("Enter Quantity: "))
        found=False
        for i in self.sales_history:
            if name in i:
                found=True
                if quan<=i[name]:
                    print("Product Returned Succesfully")
                    self.inventory[name][0]+=quan
                else:
                    print("Bahut Tez Ho Rahe Ho")
        if found==False:
                print("Ye To Hampe Heyi No")
        print("-------------------------------------")

cust1 = customer()

cust1.login()
cust1.Display()
cust1.Cart()
cust1.view()
cust1.Bill()
cust1.Place_order()

sell1 = seller()
sell1.login()
sell1.Display()
sell1.add_product()
sell1.sell_prduct()
sell1.return_product()
