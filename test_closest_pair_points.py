#test_closest_pair_points.py
#pytest file for testing closest pair points

#imports
from closest_pair_points import *
from points import *
from math import *

# content of test_class.py
class TestClass:

    #tests if the closest pair will find the closest points and their distance
    def test_closest_pair(self):
        #list of points variable
        point_list = []
        #populate the variable with points
        point_list.append(Point(1,2))
        point_list.append(Point(1,4))
        point_list.append(Point(2,2))
        point_list.append(Point(9,2))

        #get the result from the function
        result = Closest_Pair.Closest_Pair(point_list)

        #check if the first point is correct
        assert str(result[0]) == "(1,2)"

        #check if the second point is correct
        assert str(result[1]) == "(2,2)"

        #check if the distance is correct
        assert isclose(result[2], 1, abs_tol=1e-1)
