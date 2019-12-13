def getListFromFile(fileName):
    infile = open(fileName, 'r')
    rData = [line for line in infile]
    infile.close()
    return rData

def createSortedFile(data, fileName):
    data.sort()
    outfile = open(fileName, 'w')
    outfile.writelines(data)
    outfile.close()

statesList = getListFromFile('States.txt')
createSortedFile(statesList, 'StatesAlpha.txt')