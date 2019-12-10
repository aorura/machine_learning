file = open('test.txt', 'w')
file.write('hello')
file.close()

file2=open('test.txt', 'r')
str=file2.read()
print('read str1L ', str)
file2.close()
