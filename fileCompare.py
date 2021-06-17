#TO DO ~ Add comments

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
                                        print("line: " +  str(countOne) + " " + str(countTwo))
                                        print("New: " + str(lineOne))
                                        print("Old: " + str(lineTwo))
                                    break   
                            countTwo = 0
                        f1.close()                                       
                        f2.close() 
