import os
if os.path.exists("text.txt"):
    os.remove("text.txt")
else:
    print("file doesnt exist.")
new_file = open("txt.txt", 'x')
new_file.close()
a_file = open("txt.txt", 'w')
a_file.write("Look! im a new file!!")
a_file.close()
read_file=open("txt.txt", 'r')
print(read_file.read())
read_file.close()