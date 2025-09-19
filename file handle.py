file1 = open('codingal.txt', 'r')
print(file1.read())
file1.close()

file2 = open('codingal.txt', 'w')
file2.write('Coding is soooooo cool!')
file2.close()

file1 = open('codingal.txt', 'r')
print(file1.read())
file1.close()

file2 = open('codingal.txt', 'a')
file2.write('codingal is on a mission, to teach schoolkids.')
file2.close()

file1 = open('codingal.txt', 'r')
print(file1.read())
file1.close()