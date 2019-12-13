infile = open('VPres.txt', 'r')
vicePresList = {line for line in infile}
infile.close()

infile2 = open('USPres.txt','r')
presList = {line for line in infile2}
outfile = open('Both2.txt', 'w')
outfile.writelines(vicePresList.intersection(presList))
infile2.close()
outfile.close()