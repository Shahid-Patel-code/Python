class Person:
    def __init__(self):
        self.name=input("Enter Your Name: ")
        # self.age=int(input("Enter Your Age: "))
        # self.number=int(input("Enter Your Phone Number: "))

class Detail:
    def __init__(self):
        choose=False
        num=1
        mode=["Roadway","Airway"]
        for i in mode:
                print(f"{num}: ",i)
                num+=1
        while True:
            self.mode=input("Enter Mode of Travel: ")
            if self.mode in mode:
                print("This Way IS Available")
                break
            elif self.mode in mode:
                self.passport=int(input("Enter Your Passport Number: "))
                break
            else:
                print("This Method Is Not Availabe")
    def Validate(self):
        name=False
        age=False
        number=False
        passport=False
        for i in self.name:
            if i.isalpha() or i.isspace():
                name=True
            else:
                name=False
        print(self.name)
class Tourist(Person,Detail):
    def __init__(self):
        print("Name: ",self.name)
        print("Age: ",self.age)
        print("Phone Number: ",self.number)
        print("Travel Mode: ",self.mode)
class Manegment(Tourist):
    def __init__(self):
        pass

o=Person()
o1=Detail()
o1.Validate()
