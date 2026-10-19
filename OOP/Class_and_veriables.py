# Write a program to count how many object have been created for a class

# write a class student with instance veriable name and marks and one class veriable college name
# accept and print detaile of student using instance method

class student: 
    colleg="Goat Khalil College"
    def accept(self):
        self.name=input("Enter Your Name: ")
        self.marks=int(input("Enter Your Marks: "))
    def display(self):
        print(f"-----{student.colleg}-----")
        print("Name: ",self.name)
        print("Marks: ",self.marks)

obj=student()
obj.accept()
obj.display()
obj1=student()
obj.accept()
obj.display()

