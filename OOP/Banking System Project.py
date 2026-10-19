class Bank:
    Bank_Name = "GOAT BANK OF SARS-NAGAR"

    def __init__(self):
        self.Balence = 10000

    def Deposit(self, amount):
        print("-----------------------------")
        print(Bank.Bank_Name)
        print("-----------------------------")

        self.Balence += amount
        print("Balance:", self.Balence)
        print("Amount added successful!")
        print("-----------------------------")

    def Withdraw(self, amount):
        print("-----------------------------")
        print(Bank.Bank_Name)
        print("-----------------------------")

        if amount >= self.Balence:
            self.Balence -= amount
            print("Amount withdraw successful!")
            print("Balance:", self.Balence)
        else:
            print("Insufficient Balance")

        print("-----------------------------")

    def Transfer(self, obj):
        print("-----------------------------")
        print(Bank.Bank_Name)
        print("-----------------------------")

        trans = int(input("Enter Transfer Amount: "))

        if trans <= self.Balence:
            self.Balence -= trans
            obj.Balence += trans

            print("Receiver Balance:", obj.Balence)
            print("Your Balance:", self.Balence)
            print("Balance Transfer successful!")
        else:
            print("Insufficient Balance")

        print("-----------------------------")

    def show(self):
        print("-----------------------------")
        print(Bank.Bank_Name)
        print("Balance:", self.Balence)
        print("-----------------------------")


Account = {}
num = int(input("How Many Accounts do you want to create: "))

for i in range(1, num + 1):
    acc = input(f"Enter {i} Name: ")
    Account[acc] = Bank()

Name = input("Enter Your Name: ")
if Name not in Account:
    print("Account Not Found")
    exit()

user = Account[Name]
while True:

    print("""
1. Deposit
2. Withdraw
3. Transfer
4. Show Balance
5. Exit
""")

    choice = int(input("Enter choice: "))

    if choice == 1:
        amount = int(input("Enter amount: "))
        user.Deposit(amount)

    elif choice == 2:
        amount = int(input("Enter amount: "))
        user.Withdraw(amount)

    elif choice == 3:

        receiver_name = input("Enter receiver name: ")

        if receiver_name in Account:
            user.Transfer(Account[receiver_name])
        else:
            print("Receiver account not found!")

    elif choice == 4:
        user.show()

    elif choice == 5:
        print("Thank You!")
        break

    else:
        print("Invalid Choice!")
