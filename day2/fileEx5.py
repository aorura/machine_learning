infile = open("data/File1.txt", 'r')
firstSet = {line for line in infile}
infile2=open('data/File2.txt','r')
secondSet={line for line in infile2}
infile.close()
infile2.close()

outfile=open("data/Union.txt",'w')
outfile.writelines(firstSet.union(secondSet))
outfile.close()

outfile = open('data/intersection.txt','w')
outfile.writelines(firstSet.intersection(secondSet))
outfile.close()

outfile=open('data/Difference.txt','w')
outfile.writelines(firstSet.difference(secondSet))
outfile.close()