my_dict = {}
word = int(input("Enter a number, 1 - 3 and get a prize"))
my_dict = {1:'200 million ', 2:'89 cats', 3:'1 trillion baht'}
if word == 1 :
    print(my_dict[1])
elif word == 2 :
    print(my_dict[2])
else:
    print(my_dict[3])
if word > 3:
    print("Please do number 1,2,3. Not above")
    