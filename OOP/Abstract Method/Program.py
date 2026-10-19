from abc import ABC, abstractmethod
class Payment:
    @ abstractmethod
    def pay(self,amount):
        pass
class creditcardpayment(Payment):
    def pay(self,amount):
        self.amount=amount
        print("Total Amount Paid By Credit Card: ",self.amount)

class upipayment(Payment):
    def pay(self,amount):
        self.amount=amount
        print("Total Amount Paid By UPI: ",self.amount)

obj=creditcardpayment()
obj.pay(20000)
obj1=upipayment()
obj1.pay(40000)
