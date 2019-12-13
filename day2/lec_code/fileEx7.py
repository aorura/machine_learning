infile = open('Un.txt','r')
listOfRecords = [line.rstrip() for line in infile]
infile.close()

for i in range(len(listOfRecords)):
    listOfRecords[i] = listOfRecords[i].split(',')
    listOfRecords[i][2] = eval(listOfRecords[i][2])
    listOfRecords[i][3] = eval(listOfRecords[i][3])
print(listOfRecords)

def countrySize(country):
    return country[3]

listOfRecords.sort(key=countrySize, reverse=True)
print('\n{0:20}{1:9}'.format('Country', 'Area'))
for i in range(5):
    print('{0:20}{1:9}'.format(listOfRecords[i][0], listOfRecords[i][3]))

outfile = open('Area.txt','w')
for country in listOfRecords:
    outfile.write(country[0] + ', '+ str(country[3])+'\n')
outfile.close()