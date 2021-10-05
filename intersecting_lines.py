#Function to find Line Segment Intersections
#   Find the intersections between a given set of line segments.
import math
from lines import *
from points import *

#function find_intersections runs to find the intersection points and formats them into a string to be saved to a file later
def find_intersections(data_array):

    #run find all intersecting
    lists = Intersections.find_all_intersecting(data_array)

    #Write result to this string that will print int txt file
    result = "Intersections From a Given Set of Line Segments:\n\n"

    for i in lists:
        result = result + str(i[0]) + " INTERSECTS " + str(i[1]) + " AT " + str(i[2]) + "\n"

    return result

class Intersections:
    #function find_all_intersecting calculates to find the intersecting points
    def find_all_intersecting(data_array):
        #create a list to hold all intersecting results 2d array
        lists = []
        #create an array to hold each of the data values for each intersection
        result = ["","",""]
        

        #nested for loop to find which intersect
        for i in range(len(data_array)):
            for j in range(len(data_array)):
                if(j > i):
                    result[0] = data_array[i]
                    result[1] = data_array[j]
                    result[2] = data_array[i].intersects(data_array[j])
                    if(result[2] != None ):
                        lists.append([result[0],result[1],result[2]])

        return lists


