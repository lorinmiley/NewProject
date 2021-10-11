#test_main.py 
#pytest file for testing main.py functionality

#imports
from _main_ import *
import sys
# content of test_class.py
class TestClass:

    #tests if the user can input a filename as the 3rd statement entered
    #def test_inputfilename(self):
     #   #simulates running input python3 _main_.py pair_points.py
      #  #the second value input "pair_points.py" is the filename and this tests if our main function can return it.
       # sys.argv = ["_main_.py", "pair_points.txt"]
        #assert get_filename() == "pair_points.txt"

    #tests if the function array_to_point can convert an array to a list of points
    def test_array_to_point(self):
        #create a sample array how the problem will be formatted
        data_array = ["Pair of Points", "1 2", "3 4", "5 6"]
        lists = array_to_points(data_array)
        #check if it deletes the first element and makes a matching array (tested as string for formatting)
        assert str(lists) == "[(1,2), (3,4), (5,6)]"

    #tests if the function array_to_point can convert an array to a list of points
    def test_array_to_lines(self):
        #create a sample array how the problem will be formatted
        data_array = ["Pair of Points","_Line_", "1 2", "3 4", "_Line_", "5 6", "12 -9"]
        lists = array_to_lines(data_array)
        #check if it deletes the first element and makes a matching list array (tested as string for formatting)
        assert str(lists) == "[[(1,2),(3,4)], [(5,6),(12,-9)]]"

    
   

    