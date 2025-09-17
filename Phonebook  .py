import sys
def initial_phonebook():
    rows, cols = int(input("To start, please enter the number of contact:")),5
    phonebook =[]
    print(phonebook)
    for i in range(rows):
        print("Enter contact %d details in the following order only. :"% (i+1))
        print("Note:* (indicates mandatory fields.)")
        temp =[]
        for j in range(cols):
            temp.append(str(input ("Enter name.")))
       
            sys.exit( "Name is a mandatory field, please enter.")
        if j == 1:
            temp.append(int(input("Please add a number in this section.*:")))
            
        if j ==2:
            temp.append(int(input("E-mail adress goes here (This is not mandatory.): ")))
            if temp[j] == '' or temp[j] == ' ':
                temp[j]=None
        if j ==3:
            temp.apppend(int(input("Date of birth dd/mm/yy :")))
            if temp[j] == '' or temp[j] == ' ':
                temp[j]=None
        if j==4:
            temp.append(int(input("enter one of these, Family/Friend/Work/Classmate/Teacher/Spouse/others. : ")))
            if temp[j] == '' or temp[j] == ' ':
                temp[j]=None
    phonebook.append(temp)
    print(phonebook)
    return phonebook
def menu():
    print("______________________________________________________________")
    print("Smartphone Directory", flush=False)
    print("______________________________________________________________")
    print("1. Add a new contact")
    print("2. Remove an existing contact")
    print("3. Delete all contacts")
    print("4. Search for a contact")
    print("5. Display all contacts")
    print("6. Exit phonebook")
    choice = int(input("Enter your choice ::"))
    return choice
def contact(pb):
    dip = []
    for i in range(len(pb[0])):
        if i == 0:

            dip.append(input("Enter name"))
        if i == 1:

            dip.append(input("Enter number"))
        if i == 2:

            dip.append(input("Enter Email"))
        if i == 3:

            dip.append(input("dd/mm/yy"))
        if i == 4:

            dip.append(input("Category - friend / family / teacher / classmate / spouse "))
    pb.append(dip)
    return pb
def remove(pb):
    query = str(
        print("Please enter a name you would like to remove."))
    temp = 0
    for i in range(len(pb)):
        if query == pb[i] [0]:
            temp += 1
        print(pb.pop[i])
        print("This person has been removed.")
        return pb
    if temp == 0:
        print("Sorry this person does not exist / or is invalid. ")
def delete(pb):
    return pb.clear()
def searchexist(pb):
    choice = (int(input("Enter search criteria\n\n\n 1. Name\n2. Number\n3. Email-id\n4. DOB\n5. Category(Family/Friends/Work/Others)\ \nPlease enter:")))
    temp = []
    check = -1
    if choice == 1:
        query = int(input("Please enter contact's name to search"))
        for i in range(len(pb)):
            if query == pb[i][0]:
                check = i
                temp.append (pb[i])
