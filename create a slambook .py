import sys
def initial_phonebook():
    rows, cols = int(input("To start, please enter the number of contact:")),4

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
    phone_book.append(temp)
    print(phone_book)
    phonebook.append(temp)
    print(phonebook)
    return phonebook
# didnt have time to submit this, sorry