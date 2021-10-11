#readwrite.py
#This file holds all the necessary functions for reading the points from a text file of a specific type
#and writing the results to another file.

#read_txt function you input a file and it parses it into an array
from datetime import datetime
# Import the os module 
import os
#read_txt function reads an input file and parses it into an array it will return
from _main_ import *
from errors import *

#read_txt function reads an input file and parses it into an array it will return
def read_txt(filename):
    if filename=="":
        raise NoUserInput()
        
    #try to read file
    try:
        # get current working directory and add folder and filename to current working directory path 
        print(os.getcwd())
        cwd = os.getcwd() + '/input/' + filename
        print(cwd)
        inputfile = open(cwd, 'r')
        Lines = inputfile.readlines()
        data_array = []
        
        #convert the input string into an array where each row is an element
        for line in Lines:
            data_array.append(line.strip())
        inputfile.close()
    except FileNotFoundError:
        raise FileNotFoundError
    return data_array
    
    


#write_txt function takes in an input string and saves it to a txt file with current date and time 
def write_txt(result):
    #create a unique filename based on the timestamp
    filename = datetime.now().strftime("%m-%d-%Y_%H:%M:%S") + "_results.txt"
    #set that filename to the output directory
    outputfilename = "output/" + filename

    #try catch for attempting to write to file, throw an error if it fails
    try:
        f= open(outputfilename, "w+")
        f.write(result)
        f.close()
        print("\nResults created in file: " + outputfilename)
        return filename
    except:
        print("Failed to create file!!")
        return

