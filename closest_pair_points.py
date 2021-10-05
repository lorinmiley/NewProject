#closest_pair_points.py
#this file finds the closest pair of points and returns the resulting value as a formatted string

#imports
from points import *

#function calculate_closest will find the closest two points from a list of class type points
def calculate_closest(list_points):
    #initialize result variable to return later
    result = ''

    #set closest to an array holding the closest pair of points and the distance
    closest = Closest_Pair.Closest_Pair(list_points)

    #formatting the results which will later be written to a file
    for i in list_points:
        result = result + str(i) + "\n"
    result = "Closest Pair of Points Results:\n\nData Points:\n" + result + "\nClosest Pair of Points: \n" + str(closest[0]) + " " + str(closest[1]) + ")\n\nDistance: " + str(closest[2])

    #return the result as a formatted string
    return result


class Closest_Pair:

    #function __init__ will find the closest pair of points
    def Closest_Pair(list_points):
        #create array to later return
        result = []

        #starting values of comparing the first two points
        smallest = list_points[0].distance(list_points[1])
        result.append(list_points[0])
        result.append(list_points[1])
        result.append(smallest)
        
        #nested for loop to find distance
        for i in range(len(list_points)):
            for j in range(len(list_points)):
                if(j > i):
                    if(list_points[i].distance(list_points[j]) < smallest):
                        smallest = list_points[i].distance(list_points[j])
                        result[0] = list_points[i]
                        result[1] = list_points[j]
                        result[2] = smallest
        
        #return two closest points and their distance 
        return result


