try:
    n,nn= int(input("enter a number, divided by a comma."))
    result = n / nn
except ZeroDivisionError:
    print("Division by zero is not valid !!!!!!!!!!!!")
except SyntaxError:
    print("Comma missing !!!!! (do as told like this: 10,30)")
except:
    print("wrong output")
else:
    print("No exceptions")
finally:
    print("this will execute no matter what")