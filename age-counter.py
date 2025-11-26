try:
          n = int(input("enter your age to see if its even or odd! :    "))
          if n%2==0:
                  print("even!")
          elif n%2==1:
                  print("odd!")
except ValueError:
          print("Enter a actual age. ( ie [] no decimals [] no words ), an REAL age")
