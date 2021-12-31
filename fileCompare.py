# this function takes two folders containing files with the same names and compares those files

import filecmp
import os.path
import sys


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


ignoreList = [
    " ",
]


def ignoreDifferences(lineOne, lineTwo):
    # this function takes two lines of code and returns a boolean on whether the change is significant
    # considerations of blank lines is intentionally ignored, this should be considered in main()
    assert(isinstance(lineOne, str), isinstance(lineOne, str))  # verify input is a string
    # find every difference between the two lines
    if len(lineOne) > len(lineTwo):
        longerString, shorterString = lineOne, lineTwo
    else:
        longerString, shorterString = lineTwo, lineOne
    # create a list of indexes where the longer string has new items
    diffIndex = []
    indexShift = 0
    for i in range(len(longerString)):
        if i + indexShift < len(shorterString):
            if longerString[i] != shorterString[i + indexShift]:
                diffIndex.append(i)
                indexShift += 1
    # see if any of the added/removed items have insignificant changes, if so True is returned
    for i in diffIndex:
        if longerString[i] not in ignoreList:
            return False
    return True

if __name__ == "__main__":
    directoryOne = ""
    directoryTwo = ""
    try:
        if("-h" == sys.argv[1]):
            print("First arg is dir 1")
            print("Second arg is dir 2")
        else:
            directoryOne = sys.argv[1]
            print(directoryOne)
            directoryTwo = sys.argv[2]
            print(directoryTwo)
    except IndexError:
        print("IndexError")

    for filenameOne in os.listdir(directoryOne):
            for filenameTwo in os.listdir(directoryTwo):
                if(filenameOne == filenameTwo):
                    result = filecmp.cmp(directoryOne + "/" + filenameOne, directoryTwo + "/" + filenameTwo, shallow=False)
                    if(result == False):
                        print('\n')
                        print(print(bcolors.HEADER + "------------------------" + filenameOne + "------------------------" + bcolors.OKCYAN))
                        print('\n')
                        f1 = open(directoryOne + "/" + filenameOne, "r")
                        f2 = open(directoryTwo + "/" + filenameTwo, "r")
                        countOne = 0
                        countTwo = 0

                        linesOne = f1.readlines()
                        linesTwo = f2.readlines()

                        #TO DO ~ This doesn't work very well if a space was added to a file, but a majority of the files contents are the same
                        #Add modifications to handle this...
                        for lineOne in linesOne:
                            countOne += 1
                            for lineTwo in linesTwo:
                                countTwo += 1
                                if(countOne == countTwo):
                                    if lineOne == lineTwo:
                                        break
                                    else:
                                        if not ignoreDifferences(lineOne, lineTwo):
                                            print("line: " + str(countOne) + " " + str(countTwo))
                                            print("New: " + str(lineOne))
                                            print("Old: " + str(lineTwo))
                                    break
                            countTwo = 0
                        f1.close()
                        f2.close()
