sa = int(input("Type in the attendence of student"))
mc = input("Enter your medical cause.((y/n))")
if mc == "y":
    print("Allowed")
else:
    if sa>=75:
        print("Allowed.")
    else:
        print("Not allowed.")