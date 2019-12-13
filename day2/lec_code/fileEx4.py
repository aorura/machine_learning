infile = open('VPres.txt', 'r')
vicePresList = [line for line in infile]
infile.close()

infile2 = open('USPres.txt','r')
outfile = open('Both.txt', 'w')

for person in infile2:
    if person in vicePresList:
        outfile.write(person)
infile2.close()
outfile.close()