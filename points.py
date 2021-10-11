#points.py 
#this class is created for holding a point and performing relevant operations

#imports
import math

#point class
class Point:
    #function __init__ will set x and y values
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    #setter for x value
    def setX(self, x):
        self.x = x
    #setter for y value
    def setY(self, y):
        self.y = y

    #getter for X
    def getX(self):
        return self.x
    #getter for y
    def getY(self):
        return self.y

    #function distance will use the distance formula to find the distance from the point to an input one
    def distance(self, other):
        dx = self.x - other.x
        dy = self.y - other.y
        return math.sqrt(dx**2 + dy**2)

    #function __repr__ will format the output
    def __repr__(self):
        return '({},{})'.format(self.x, self.y)



        #this is Jacob