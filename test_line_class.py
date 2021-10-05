#test_line_class.py
#pytest file for testing lines.py functionality

#imports
from points import *
from lines import *
from math import *

# content of test_class.py
class TestClass:

    #tests if a line is initialized with the two input points
    def test_set(self):
        l1 = Line(Point(3,7),Point(2,3))
        assert str(l1.p1) == str(Point(3,7))
        assert str(l1.p2) == str(Point(2,3))
    
    #tests setters for point 1 and point 2
    def test_set_points(self):
        l1 = Line(Point(3,7),Point(2,3))
        l1.setPoint1(Point(2,2))
        l1.setPoint2(Point(1,1))

        assert str(l1.p1) == str(Point(2,2))
        assert str(l1.p2) == str(Point(1,1))

    #tests getters for point 1 and point 2
    def test_set_points(self):
        l1 = Line(Point(3,7),Point(2,3))

        assert str(l1.Point1()) == str(Point(3,7))
        assert str(l1.Point2()) == str(Point(2,3))

    #tests getters for point 1 and point 2
    def test_slope(self):
        l1 = Line(Point(9,10),Point(99,2))

        assert isclose(l1.slope(), -0.08, abs_tol=1e-1)

    #tests getters for point 1 and point 2
    def test_length(self):
        l1 = Line(Point(3,7),Point(99,3))

        assert isclose(l1.length(), 96.1, abs_tol=1e-1)

    #test for intersection at a point
    def test_One(self):
        line1 = Line(Point(2,8),Point(2,-2))
        line2 = Line(Point(9,10),Point(-2,2))
        result = line1.intersects(line2)
        assert isclose(result.x, 2, abs_tol=1e-1) and isclose(result.y, 4.9, abs_tol=1e-1)

    #test for infinite intersection parrallel lines
    def test_Two(self):
        line1 = Line(Point(-1,-1),Point(1,1))
        line2 = Line(Point(0,0),Point(2,2))
        result = line1.intersects(line2)
        assert result == inf

    #test for no intersection
    def test_Three(self):
        line1 = Line(Point(1,1),Point(1,2))
        line2 = Line(Point(0,0),Point(1,3))
        result = line1.intersects(line2)
        assert result == None
    
    #test for intersection at one end
    def test_Four(self):
        line1 = Line(Point(1,1),Point(1,2))
        line2 = Line(Point(1,2),Point(1,5))
        result = line1.intersects(line2)
        assert result.x == Point(1,2).x and result.y == Point(1,2).y