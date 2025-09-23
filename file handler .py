file1 = open('cjhan .txt', 'r')
print(file1.read())
file1.close()

file2 = open('cjhan .txt', 'w')
file2.write('im changing..')
file2.close()

file1 = open('cjhan .txt', 'r')
print(file1.read())
file1.close()

file2 = open('cjhan .txt', 'a')
file2.write('I changed!')
file2.close()

file1 = open('cjhan .txt', 'r')
print(file1.read())
file1.close()