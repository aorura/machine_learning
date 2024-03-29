def getSetOfNewColors():
    infile = open("Pre1990.txt", 'r')
    colors = {line.rstrip() for line in infile}
    infile.close()
    infile = open("Retired.txt", 'r')
    retiredColors = {line.rstrip() for line in infile}
    infile.close()
    infile = open("Added.txt", 'r')
    addedColors = {line.rstrip() for line in infile}
    infile.close()
    colorSet = colors.difference(retiredColors)
    colorSet = colorSet.union(addedColors)
    return colorSet


def createFileOfNewColors(setOfNewColors):
    orderedListOfColors = sorted(setOfNewColors)
    orderedListOfColorsString =('\n').join(orderedListOfColors)
    outfile = open("NewColors.txt", 'w')
    outfile.write(orderedListOfColorsString)
    outfile.close()

    
setOfNewColors = getSetOfNewColors()
createFileOfNewColors(setOfNewColors)
