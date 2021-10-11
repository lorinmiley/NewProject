#Computational Geometry Project
#The purpose of this project is to create a python application where the user can input a text file
#   that contains a header with a type of problem to solve, line segment intersection, closest pair points,
#   convex hull, or largest empty circle followed by a given set of points seperated by line with a space seperating x and y

#Programmers:
#   Humberto Ortega
#   Lorin llene Miley
#   Jacob A Hendricks
#   Hope Elizabeth Fetrow

#imports
import os
import sys
from points import *
from lines import *
from readwrite import *
from closest_pair_points import *
from intersecting_lines import *
from convex_hull import *
from largest_empty_circle import *

from errors import *


# function to get problem choice from user 
# which is the text file to read from 
def display_menu():
    u = ""    
    u = input("Enter file name")
    return u


#function array_to_points converts an array into a list of points (can be used for 3 out of the 4 problem types)
def array_to_points(data_array):
    #Removes the first element of the array since we dont need it anymore (problem type)
    data_array.pop(0)

    #create a list to hold all the points from the given array
    pointlist = []

    #loop through each element in data_array and append point list with each x and y value
    for i in data_array:
        points = i.split()
        singlePoint = Point(int(points[0]),int(points[1]))
        pointlist.append(singlePoint)

    return pointlist

#function array_to_lines converts an array of sectioned points into a list of line segments
def array_to_lines(data_array):
    #Removes the first element of the array since we dont need it anymore
    data_array.pop(0)

    #create a list to hold all the lines
    linelist = []

    #initialize temp variable to hold one line data
    oneline = [0,0]

    firstpoint = 1

    #for loop to loop through each item in the array and push every two points into a line list
    for i in data_array:
        if(i != "_Line_"):
            points = i.split()
            if(firstpoint == 1):
                oneline[0] = Point(int(points[0]),int(points[1]))
                firstpoint = 0
            elif(firstpoint == 0):
                oneline[1] = Point(int(points[0]),int(points[1]))
                linelist.append(Line(oneline[0],oneline[1]))
                firstpoint = 1   

    return linelist
    
def call_problem(data_array):
    #holds string that will be returned to print to a file
    results = ''

    #else if the first line of the file asks for closest pair of points run this
    if(data_array[0] == 'Closest Pair Of Points'):
        results = calculate_closest(array_to_points(data_array))

    #else if the first line of the file asks for the Convex Hull
    elif(data_array[0] == 'Convex Hull'):
        results = find_convex_hull(array_to_points(data_array))
        
    #else if the first line of the file asks for the Largest empty circle
    elif(data_array[0] == 'Largest Empty Circle'):
        results = find_largest_empty_circle(array_to_points(data_array))
        
    #if the first line of the file asks for intersection run this code
    elif(data_array[0] == 'Line Segment Intersection'):
        results = find_intersections(array_to_lines(data_array))

    #write_txt(results)
    return results

#main class
class Main:
    @staticmethod
    def __init__(*args: str) -> None:

        
        try:
            #get the user input filename
            filename = display_menu()
            #read text file 
            data_array = read_txt(filename)
            #call appropiate problem class 
            results = call_problem(data_array)
        except NoUserInput:
            print("Nothing entered, enter a file name: ")
            Main()
        except FileNotFoundError:
            print("File was not found, enter a file name: ")            
            Main()

        return
if __name__ == '__main__':
    Main()


