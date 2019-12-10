def displayWithForLoop(file):
    infile=open(file,'r')
    for line in infile:
        print(line, end='')
    infile.close()

def getList(file):
    infile=open(file, 'r')
    print([ line.rstrip() for line in infile ])
    infile.close()

file = 'data\FirstPresidents.txt'
displayWithForLoop(file)
getList(file)