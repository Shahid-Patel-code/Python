''' Develop a Python program to manage members of three different clubs: Science,
 Arts, and Commerce using the set data structure.
The system should be menu-driven and allow the user to perform various 
operations on club members. Each club should store only unique member names.
The program should provide the following functionalities:
Display all members of each club. 
Display a combined list of all unique members across all clubs. 
Display members who are present in all three clubs. 
Add a new member to a specific club with the following condition: 
If the member already exists in that club, display an appropriate message. 
Remove a member from all clubs with the following condition: 
If the member does not exist in any club, display a warning message. 
Check whether a person is a member of any club and display: 
The club name(s) they belong to 
If not found, display "Not a member of any club" 
Display members who belong to only one club. 
Display members who belong to exactly two clubs. 
Display the total number of members in each club. 
From a given list of students, display those who are not part of any club. 
Identify the club having the highest number of members
If two or more clubs have equal members, display all of them.
Exit the program
The program should ensure that duplicate entries are not allowed and operations 
are performed efficiently using set properties.'''

Science={'Rahul', 'Amit', 'Sneha'}    
Arts={'Sneha', 'Priya', 'Kiran'}
Commerce= {'Amit', 'Kiran', 'Rohit'}

Science = {'Rahul', 'Amit', 'Sneha'}
Arts = {'Sneha', 'Priya', 'Kiran'}
Commerce = {'Amit', 'Kiran', 'Rohit'}

while True:
    print("""
--- MENU ---
1. Display Members
2. Show All Unique Members
3. Show Common Members
4. Add Member
5. Remove Member from ALL clubs
6. Check Membership
7. Members in Only One Club
8. Members in Exactly Two Clubs
9. Count Members
10. Students Not in Any Club
11. Club with Maximum Members
12. Exit
""")

    choice = int(input("Enter your choice: "))

    # 1. Display all members
    if choice == 1:
        print("Science:", Science)
        print("Arts:", Arts)
        print("Commerce:", Commerce)

    # 2. All unique members
    elif choice == 2:
        union = Science | Arts | Commerce
        print("All unique members:", union)

    # 3. Common members in all three clubs
    elif choice == 3:
        common = Science & Arts & Commerce
        print("Common members in all clubs:", common)

    # 4. Add member
    elif choice == 4:
        name = input("Enter name: ")
        print("1. Science\n2. Arts\n3. Commerce")
        club = int(input("Choose club: "))

        if club == 1:
            if name in Science:
                print("Member already exists in Science")
            else:
                Science.add(name)
                print("Added successfully")

        elif club == 2:
            if name in Arts:
                print("Member already exists in Arts")
            else:
                Arts.add(name)
                print("Added successfully")

        elif club == 3:
            if name in Commerce:
                print("Member already exists in Commerce")
            else:
                Commerce.add(name)
                print("Added successfully")

        else:
            print("Invalid choice")

    # 5. Remove member from ALL clubs
    elif choice == 5:
        name = input("Enter name: ")

        if name not in Science and name not in Arts and name not in Commerce:
            print("Member not found in any club")
        else:
            Science.discard(name)
            Arts.discard(name)
            Commerce.discard(name)
            print("Removed from all clubs")

    # 6. Check membership
    elif choice == 6:
        name = input("Enter name: ")
        clubs = []

        if name in Science:
            clubs.append("Science")
        if name in Arts:
            clubs.append("Arts")
        if name in Commerce:
            clubs.append("Commerce")

        if clubs:
            print(f"{name} belongs to: {', '.join(clubs)}")
        else:
            print("Not a member of any club")

    # 7. Members in only one club
    elif choice == 7:
        only_science = Science - (Arts | Commerce)
        only_arts = Arts - (Science | Commerce)
        only_commerce = Commerce - (Science | Arts)

        result = only_science | only_arts | only_commerce
        print("Members in only one club:", result)

    # 8. Members in exactly two clubs
    elif choice == 8:
        sc_ar = (Science & Arts) - Commerce
        ar_co = (Arts & Commerce) - Science
        sc_co = (Science & Commerce) - Arts

        result = sc_ar | ar_co | sc_co
        print("Members in exactly two clubs:", result)

    # 9. Count members in each club
    elif choice == 9:
        print("Science:", len(Science))
        print("Arts:", len(Arts))
        print("Commerce:", len(Commerce))

    # 10. Students not in any club
    elif choice == 10:
        students = set(input("Enter student names (comma separated): ").split(","))
        all_members = Science | Arts | Commerce
        not_members = students - all_members
        print("Students not in any club:", not_members)

    # 11. Club with maximum members
    elif choice == 11:
        max_count = max(len(Science), len(Arts), len(Commerce))

        print("Club(s) with maximum members:")
        if len(Science) == max_count:
            print("Science")
        if len(Arts) == max_count:
            print("Arts")
        if len(Commerce) == max_count:
            print("Commerce")

    # 12. Exit
    elif choice == 12:
        print("Exiting program...")
        break

    else:
        print("Invalid choice")

