infile = open('data/VPres.txt', 'r')
vicePresList=[line for line in infile]
infile.close()

infile2 = open('data/USPres.txt', 'r')
outfile = open('data/Both.txt', 'w')

for person in infile2:
    if person in vicePresList:
        outfile.write(person)
        print(person, end='')

infile2.close()
outfile.close()