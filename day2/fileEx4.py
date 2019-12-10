infile = open('VPres.txt', 'r')
vicePresList=[line for line in infile]
infile.close()

infile2 = open('USPres.txt', 'r')
outfile = open('Both.txt', 'w')
