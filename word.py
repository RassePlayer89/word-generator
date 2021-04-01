import sys

## print("Number of arguments: " + str(len(sys.argv)) + " argument(s)")
## print("Argument List:" + str(sys.argv))

if ( len( sys.argv) < 3):
    print("Usage: " + sys.argv[0] + " characters and magic letter")
    quit(0)

iStr = sys.argv[1]
iMagic = sys.argv[2]
iStrlen = len(iStr)
inputArray = list( iStr )
wordsFound = []

print("Finding words that can be generated from characters: " + iStr)
##set the file1 to open the linux.words word list
file1 = open('', 'r')
Lines = file1.readlines()

for line in Lines:
    ## print("Mathing {}".format(line.strip()))
    if len(line.strip()) < 4:
        continue

    currWord = line.strip().lower()
    wordArray = list( currWord ) 
        
    ## print( wordArray )
    ## print("Word length " + str(wordlen) )

    if not iMagic in wordArray:
        continue

    mybool = True

    for x in wordArray:
        ## print( x )
        if not x in iStr:
            mybool = False
            break
                
    if mybool == True:
        if not currWord in wordsFound:
            print("Match found: " + currWord )
            wordsFound.append( currWord )
        

