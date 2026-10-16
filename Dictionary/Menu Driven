# student={"name": "shahid","age":19}
# print (student)
# print("name:",student["name"])
# student["city"]="Ahmednagar"
# print(student)
# student["name"]="Markus"
# print(student)
# del student["name"]
# print(student)

# print(student.keys())
# print(student.values())


student={"Shahid":86, "Khalil":89}

while True:
    print("""
1. Add a name
2. view student
3. search student
4. update marks
5. exit
""")
    choice=int(input("Enter your choice: "))
    if choice==1:
        name=input("Enter name: ")
        marks=int (input("Enter Marks: "))
        student["name"]= marks
        print("Student Added")

    elif choice==2:
        print(student.keys())

    elif choice==3:  
        name=input("Enter Name to search: ")
        if name in student:
            print(f"{name} Exist in Dictionary")
        else: 
            print(f"{name} doesnt exist")

    elif choice==4:
        name=input("Enter Name: ")
        if name in student:
            marks=int(input("Enter marks: "))  
            student[name]=marks
            print("Update succesfull")
        else:
            print("Name Not in dictionsry")    
    elif choice==5:
        print("Existing prograam")
        break  
