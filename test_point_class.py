#test_point_class.py
#pytest file for testing points.py functionality

#imports
from points import *
from math import *

# content of test_class.py
class TestClass:

    #tests if a point is initialized that it will hold the correct input x and y values
    def test_set(self):
        p1 = Point(3,7)
        assert p1.x == 3
        assert p1.y == 7
    
    #test set for x
    def test_set_x(self):
        p1 = Point(9,6)
        p1.setX(8)
        assert p1.x == 8

    #test set for y
    def test_set_y(self):
        p1 = Point(9,6)
        p1.setY(2)
        assert p1.y == 2

    #test get for x
    def test_get_x(self):
        p1 = Point(9,6)
        assert p1.getX() == 9

    #test get for y
    def test_get_y(self):
        p1 = Point(9,6)
        assert p1.getY() == 6

    #test distance function check
    def test_distance(self):
        p1 = Point(1,1)
        p2 = Point(2,3)
        #checks if it is approximately 2.23 distance
        assert isclose(p1.distance(p2), 2.23, abs_tol=1e-1)

    #tests if the __repr__ will return the correctly formatted point representation
    def test_format_output_point(self):
        p1 = Point(4,5)
        assert str(p1) == "(4,5)"
    


    