# Develop a Shopping List Manager using Python that allows a user to manage items required for 
# shopping. The program should allow users to add items, remove items, display the list, search 
# items, and count the total number of items using a list data structure.
List=[]
while(True):

    print("""------ Shopping List Manager ------
1. Add Item
2. Display Items
3. Search Item
4. Remove Item
5. Count Items
6. Exit

          """)
    choice=int(input("Enter your choice: "))
    if choice==1:
        add=input("Enter name of Item: ")
        List.append(add)
        print(f"The Item {add} is added to List")
    elif choice==2:
        for i in List:
            print(i)
    elif choice==3:
        search=input("Enter name of Item: ")
        if search in List:
            print("The Item is in List")
        else:
            print("The Item is not in List")
    elif choice==4:
        name=input("Enter Name of Item: ")
        if name in List:
            List.remove(name)
            print(f"The Item {name} is removed from List")
        else:
            print(f"{name} is not in List")
    elif choice==5:
        print("The Count of Item is: ",len(List))
    elif choice==6:
        print("Exiting The Program")
        break

