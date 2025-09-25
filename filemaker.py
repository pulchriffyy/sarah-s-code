import os
os.rmdir('fileprojects')
if os.path.exists("text.txt"):
    os.remove("text.txt")
else:
    print("file doesnt exist.")
new_file = open("new_file2.txt", 'x')
new_file.close()
a_file = open("new_file2.txt", 'w')
a_file.write("Look! im a new file!!")
a_file.close()
read_file=open("new_file2.txt", 'r')
print(read_file.read())
read_file.close()
