#Develop a menu-driven Phonebook Application using Python dictionary to store contact details. 
# The application should allow the user to perform basic operations like adding, searching, 
# updating, deleting, and displaying contacts.
contact={}
search={}
while True:
    print("""===== PHONEBOOK MENU =====
1. Add new contact
2. Search contact
3. Update contact
4. Delete contact
5. Display All Contacts
6. Search by Number
7. Rename contact
8. Show recently searched contacts
9. Delete all contacts
10. Remove Specific contact
11. Exit
""")
    choice=int(input("Enter your Choice: "))
    if choice==1:
        take=int(input("How many number Contact have: "))
        name=input("Enter Name: ")
        for i in range(take):
            
            if name not in contact:
                contact[name]=[]
            num=int(input(f"Enter {i+1} Number: "))
            contact[name].append(num)
            print(f"{i+1} Number Added Succesfully")
        
    elif choice==2: 
        name=input("Enter Name: ")
        if name in contact:
            print(f"{name} is in contact")
            print(f"{name}: {contact[name]}")
            search[name]=contact[name]
        else:
            print(f"{name} not in contact")

    elif choice==3:
        name=input("Enter Name: ")
        num=int(input("Enter Number: "))
        if name in contact:
            contact[name]=[num]
            print("Contact Updated Succesfully")
        else:
            print("No Such Name in Contact")

    elif choice==4:
        name=input("Enter Name: ")
        contact.pop(name,f"{name} not in contact")
        print("Contact Deleted Succesfully")

    elif choice==5:
        for i in contact:
            print(f"{i}: {contact[i]}")

    elif choice==6:
        num=int(input("Enter Number: "))
        for i in contact:
             if num in contact[i]:
                print("The Number is in Contact")
                print(f"{i}:{contact[i]}")
                break
        else:
            print("No Such Number in Contact")

    elif choice==7:
        name=input("Enter old Name: ")
        if name in contact:
            name2=input("Enter new Name: ")
            num=contact.pop(name)
            contact[name2]=num
            print("Contact Changed Succesfully")
        else:
             print("No Such Name in Contact")
       
    elif choice==8:
        print("---- Recently Search Contact----")
        for i in search:
            print(f"{i}: {search[i]}")

    elif choice==9:
        sure=input("Are you sure y/n: ")
        if sure=="y":
            print("contact deleted succesfully")
            del(contact)
        elif sure=="n":
            print("Thank You")
        else:
            print("Enter Valid choice Only y/n ")

    elif choice==10:
        name=input("Enter Name: ")
        if name in contact:
            num=int(input("Enter a number: "))
            if num in contact[name]:
                contact[name].remove(num)
                print("Number Deleted Succesfully")
            else:
                print("No such Number in Contact")
        else:
            print("No such Name in Contact")
            
    elif choice==11:
        print("Exiting The Program")
        break