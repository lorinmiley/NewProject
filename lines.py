#lines.py 
#this class is created for holding a line and performing relevant operations

#imports
import math
from points import *

#line class
class Line:
    #function __init__ will set x and y values
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    #setter for first point
    def setPoint1(self, p1):
        self.p1 = p1
    #setter for y value
    def setPoint2(self, p2):
        self.p2 = p2

    #getter for X
    def Point1(self):
        return self.p1
    #getter for y
    def Point2(self):
        return self.p2

    #calculates the lines length
    def length(self):
        dist_x = abs(self.p2.x - self.p1.x)
        dist_y = abs(self.p2.y - self.p1.y)
        dist_x_squared = dist_x ** 2
        dist_y_squared = dist_y ** 2
        line_length = math.sqrt(dist_x_squared + dist_y_squared)
        return line_length
	
    #calculates the lines slope
    def slope(self):
        dist_y = self.p2.y - self.p1.y
        dist_x = self.p2.x - self.p1.x
        line_slope = dist_y/dist_x
        return line_slope

    #calculates if a line intersects with another
    def intersects(self, line2):
        #place line point values into their appropriate x and y 
        x1 = self.p1.x
        x2 = self.p2.x
        x3 = line2.p1.x
        x4 = line2.p2.x
        y1 = self.p1.y
        y2 = self.p2.y
        y3 = line2.p1.y
        y4 = line2.p2.y

        #create vectors for determining points of intersection
        dx1 = x2 - x1
        dx2 = x4 - x3
        dy1 = y2 - y1
        dy2 = y4 - y3
        dx3 = x1 - x3
        dy3 = y1 - y3

        #find determinants
        det = dx1 * dy2 - dx2 * dy1
        det1 = dx1 * dy3 - dx3 * dy1
        det2 = dx2 * dy3 - dx3 * dy2

        #if one line is the same as another but in the opposite direction then we know the number of intersection points is infinite
        if(x1 == x4 and y1 == y4 and x2 == x3 and y2 == y3):
            return math.inf

        #will check if the determinent is 0 in which case, the lines are parallel
        if det == 0.0:  
            if dx1:
                if x1 < x3 < x2 or x1 > x3 > x2:
                    return math.inf  
            else:
                if y1 < y3 < y2 or y1 > y3 > y2:
                    return math.inf 

            #if the the line intersects at one of the given line segment end points return that point of intersection
            if str(self.p1) == str(line2.p1) or str(self.p1) == str(line2.p2):
                return line2.p1
            elif str(self.p2) == str(line2.p1) or str(self.p2) == str(line2.p2):
                return self.p2


            #if nothing else has run then they are parallel but do not intersect so return none since there is no intersection
            return None  

        #if the lines are found to intersect but not at any end point, perform the calculations to find the point
        s = det1 / det
        t = det2 / det

        if 0.0 < s < 1.0 and 0.0 < t < 1.0:
            return Point(x1 + t * dx1, y1 + t * dy1)

    #function __repr__ will format the output
    def __repr__(self):
        return '[{},{}]'.format(self.p1, self.p2)