def displayWithForLoop(file):
    infile = open(file, 'r')
    for line in infile:
        print(line, end='')
    infile.close()

def diplayWithList(file):
    infile = open(file, 'r')
    listData = [line.rstrip() for line in infile]
    print(listData)
    infile.close()

file = 'FirstPresidents.txt'
displayWithForLoop(file)
diplayWithList(file)