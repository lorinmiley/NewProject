#test_line_class.py
#pytest file for testing lines.py functionality

#imports
from points import *
from lines import *
from intersecting_lines import *
from math import *

# content of test_class.py
class TestClass:

    #tests if a line is initialized with the two input points
    def test_intersecting(self):
        l1 = Line(Point(2,5),Point(3,6))
        l2 = Line(Point(2,8),Point(9,10))
        l3 = Line(Point(4,0),Point(3,33))
        l4 = Line(Point(-2,-2),Point(2,2))
        l5 = Line(Point(2,4),Point(4,8))
        l6 = Line(Point(4,8),Point(8,16))

        lists = [l1,l2,l3,l4,l5,l6]
        print(str(Intersections.find_all_intersecting(lists)))
        assert str(Intersections.find_all_intersecting(lists)) == "[[[(2,8),(9,10)], [(4,0),(3,33)], (3.742489270386266,8.49785407725322)], [[(2,8),(9,10)], [(4,8),(8,16)], (4.333333333333333,8.666666666666666)], [[(4,0),(3,33)], [(2,4),(4,8)], (3.7714285714285714,7.542857142857143)], [[(2,4),(4,8)], [(4,8),(8,16)], (4,8)]]"