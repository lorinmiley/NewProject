#test_convex.py
# pytest file for testing convex_hull.py

#imports
from convex_hull import *
from points import *

#content of test_convex.py
class TestClass:

	#test for the left index method
	def test_left_index(self):
		point_list=[]
		point_list.append(Point(10,2))
		point_list.append(Point(9,8))
		point_list.append(Point(2,9))
		point_list.append(Point(1,8))
		n=Convex_hull.left_index(point_list)
		assert n == 3
		
	#test to see if the orientation method returns 2 for counterclockwise
	def test_orientation_counterclockwise(self):
		p1=(Point(0,0))
		p2=(Point(4,4))
		p3=(Point(1,2))
		n=Convex_hull.orientation(p1,p2,p3)
		assert n == 2
		
	#test to see if orientation method returns 1 for clockwise
	def test_orientation_clockwise(self):
		p1=Point(1,1)
		p2=Point(3,4)
		p3=Point(2,0)
		n=Convex_hull.orientation(p1,p2,p3)
		assert n == 1
	
	#test to see if orientation method returns 0 for collinear points
	def test_orientation_collinear(self):
		p1=Point(0,0)
		p2=Point(1,1)
		p3=Point(4,4)
		n=Convex_hull.orientation(p1,p2,p3)
		assert n == 0
	