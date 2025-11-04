string = input("Enter a word ")
c = input("enter a character ")
count = 0
for char in string:
    if c == char:
        count = count+1
print("The number of occurance",count) 