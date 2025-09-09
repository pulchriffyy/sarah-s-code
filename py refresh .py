print("star pattern \n")
for i in range(1,4):
    for j in range(i):
        print("*", end=" ")
    print("\n")
# J limit is i's value
print("inverted version. \n")
for i in range(4,1,-1):
   for j in range(i,1,-1):
        print("*", end=" ")
   print("\n")