#TO DO ~ Add comments


import filecmp
import os.path
import sys

if __name__ == "__main__":
    pathOne = ""
    pathTwo = ""
    try:
        if("-h" == sys.argv[1]):
            print("First arg is dir 1")
            print("Second arg is dir 2")
        else:
            directoryOne = sys.argv[1]
            directoryTwo = sys.argv[2]
    except IndexError:
        print("IndexError")

    for filenameOne in os.listdir(directoryOne):
            for filenameTwo in os.listdir(directoryTwo):
                if(filenameOne == filenameTwo):
                    result = filecmp.cmp(directoryOne + "/" + filenameOne, directoryTwo + "/" + filenameTwo, shallow=False)
                    if(result == False):
                        print('\n')
                        print("------------------------" + filenameOne + "------------------------")
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
                                        print("line: " + str(countOne) + " " + str(countTwo))
                                        print("New: " + str(lineOne) )
                                        print("Old: " + str(lineTwo))
                                    break   
                            countTwo = 0
                        f1.close()                                       
                        f2.close() 
