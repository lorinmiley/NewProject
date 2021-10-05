#test_read_write
#pytest file for testing readwrite.py

#imports
from readwrite import *

class TestClass:

    #tests if function read_txt can read and return a file
    #if it can read the file then it will return anything that is not None, even if the file is empty
    def test_Read(self):
        #this is an existing text file in test_txt used ../ to back out one directory since our function goes into input directory by default
        assert read_txt("../test_txt/empty.txt") != None
    

    #tests if function write_txt can create a file
    def test_Create_File(self):
        dir = write_txt("testing")
        assert os.path.exists(os.getcwd()+ "/output/" + dir) == True
        #delete the created file for cleanup
        os.remove(os.getcwd()+ "/output/" + dir)

    #tests if function write_txt can write the input string to a file
    def test_Write_File(self):
        dir = write_txt("testing")
        #check if the output file that is supposed to write "testing" did write to it by reading it
        assert read_txt("../output/" + dir) == ["testing"]
        #delete the created and written to file for cleanup
        os.remove(os.getcwd()+ "/output/" + dir)