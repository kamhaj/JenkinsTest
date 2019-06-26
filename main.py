'''
        This file contains and runs methods for reading an input file, running tests on given data
        and posting possible bugs on Azure DevOps board
'''


import pytest
import sys

#define lists for specific tests - this is the list of lists containing all of input file's data
input_list = list()

''' READ INPUT FILE '''
#read the file from input
def readFile(filename):
    file_object  = open(filename, "r")
    return file_object

#close the file
def close_file(filename):
    filename.close()

#readFile = readFile(myFilename)
readFile = readFile(sys.argv[3])



''' READ CONNECTION STRING(S) '''
#read a fragment of a connection string from a file
def read_connection_string(filename):
    for line in filename:
        if "#" in line:                     #ignore comments
            continue
        else:
            return line


#read one or two connection string from a file
def read_connection_strings(filename):
    conn_string = []
    for line in filename:
        if "#" in line or line == '\n':                    #ignore comments
            continue
        else:
            conn_string.append(line)
            # print("FIRST LINE IS: "+ str(line))
            # print("NEXT LINE IS: " + str(next(filename)))
            next_line = next(filename)
            if next_line  not in ['\n', '\r\n']:      #if not an empty line
                conn_string.append(next_line)
            else:
                conn_string.append("")
            break
    return conn_string


''' CONVERT CHUNKS OF DATA FROM INPUT FILE INTO A LIST '''
#reads an input file and creates lists (separated by blank lines in input file) for specific tests
def convert_file_to_lists(filename):
    MegaList = list()
    for line in filename:
        MegaList.append(convert_block_into_list(filename))
    return MegaList


# #read next block of data from a file, until an empty line is spotted
def convert_block_into_list(filename):
    listOfTuples = list()
    #tempTuple = list()
    for line in readFile:
        if "#" in line:                     #ignore comments
            continue
        if line not in ['\n', '\r\n']:      #if not an empty line
            tempTuple = []
            l = (line.rstrip()).split(",")
            for x in range(0, len(l)):
                tempTuple.append((l[x]).strip())
            tempTuple = (tempTuple[0], tempTuple[1:])
            listOfTuples.append((tempTuple) )
        else:
            return listOfTuples
    return listOfTuples





#connection string to the proper database, read from an input file
conn_strings = read_connection_strings(readFile)
conn_string = conn_strings[0]
conn_string2 = conn_strings[1]

#convert input file into lists of tuples
input_list = convert_file_to_lists(readFile)

#running pytest directly from python, first argument given in terminal (yaml file) is a test script file name
pytest.main([str(sys.argv[6]), "-v", "--html=index.html" , "--css=assets\\style.css"])
