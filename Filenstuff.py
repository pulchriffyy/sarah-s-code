file1=open('woah.txt','r')
file2=open('woahhwrite.txt','w')
for line in file1.readlines():
    if (line.startswith('earth')):
        print(line)
        file2.write("line") 
file1.close()