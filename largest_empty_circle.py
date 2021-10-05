#Function to find the Convex Hull
#   Given a set of points, find a largest circle with its center inside of their convex hull and enclosing none of them.

# for creating Voronoi diagram
from scipy.spatial import Voronoi
# for finding convex hull of vertices in Voronoi diagram
from scipy.spatial import ConvexHull
import numpy as np
from scipy.spatial import voronoi_plot_2d
from array import *
import math


def line(p1, p2):
    A = (p1[1] - p2[1])
    B = (p2[0] - p1[0])
    C = (p1[0]*p2[1] - p2[0]*p1[1])
    return A, B, -C


def intersection(L1, L2):
    D = L1[0] * L2[1] - L1[1] * L2[0]
    Dx = L1[2] * L2[1] - L1[1] * L2[2]
    Dy = L1[0] * L2[2] - L1[2] * L2[0]
    if D != 0:
        x = Dx / D
        y = Dy / D
        return x, y
    else:
        return False


def find_largest_empty_circle(data_array):
    # Write result to this string that will print int txt file
    result = ''
    print(data_array)

    # 1. Compute the Voronoi Diagram 𝑉𝐷 of the set of points
    # 2. Compute the Convex Hull 𝐶𝐻 of the set of points
    # 3. The center of the 𝐿𝐸𝐶 is at one of the 𝑉𝐷 vertexes inside the 𝐶𝐻
    #    or it is at an intersection between one of the 𝑉𝐷 edges and 𝐶𝐻.
    # 4. For each Voronoi vertex v do:
    #     • If v is inside CH(S) then
    #     • Compute radius of circle centered on v, update max
    #    For each Voronoi edge e do:
    #     • Compute p = e ∩ ∂CH(S)
    #     • Compute radius of circle centered on p, update max
    # 5. Return max

    # have to be able to solve if len < 4 (or is it not possible?)
    if len(data_array) >= 4:
        # 1. Compute Voronoi Diagram
        vor = Voronoi(data_array)
        # 2. Compute the Convex Hull
        hull = ConvexHull(data_array, len(data_array))

        #print(vor.vertices)
        #print(hull.simplices)

        # for min and max values, need to find a better way to do this
        x_min = 10000000000
        x_max = -10000000000
        y_min = 10000000000
        y_max = -10000000000

        # max radius (radius of largest empty circle)
        radius_max = [(-1,-1,-1)]
        radius = 0
        # closest points to vertex (points[0][0] is closest)
        # [[distance, closest_point_x_value, closest_point_y]]
        closest_point = [(100000,100000,100000)]

        # to store possible circle center coordinates with their closest points
        candidates = [[]]
        
        # Find min and max X,Y values in convex hull
        for s, t in hull.simplices:
            if(s < x_min):
                x_min = s
            if(s > x_max):
                x_max = s
            if(t < y_min):
                y_min = t
            if(t > y_max):
                y_max = t

        # pointer for loop
        p = 0

        # Find vertices of Voronoi Diagram that are inside Convex Hull
        # (these are possible centers for the circle
        for j, k in vor.vertices:
            # if vertex is inside of convex hull, then it is a candidate center 
            if (j < x_max) and (j > x_min) and (k < y_max) and (k > y_min):
                # find closest point by finding min distance between vertex and all points in CH 
                for each in hull.simplices:
                    c2 = each
                    # find distance between vertex and point 
                    distance = math.sqrt(((each[0]-j)**2)+((each[1]-k)**2))
                    # see if it replaces any of the current 3 closest points
                    if distance<closest_point[0][0]:
                        # if distance < current min distance
                        closest_point[0]=(distance,j,k)
                        # if distance > max of all mins distances 
                        if(distance>radius_max[0][0]):
                            radius_max[0]=[distance,j,k, closest_point];
                # add to list of candidate centers of largest circle
                candidates.insert(p, [j, k, closest_point[0]])            
                p = p + 1

            # increment pointer
            p = p + 1

        # Find all insersections between Voronoi edges and Convex Hull edges

        # pointers
        p = 0
        p2 = 0
        p3 = len(candidates)-1

        # for each vertex in Voronoi Diagram
        for l, m in vor.vertices[:-2]:
            # form a line by grabbing next vertex in list
            L1 = line(vor.vertices[p], vor.vertices[p + 1])
            # see if this Vornoi edge intersects with any Convex Hull edges
            for s, t in hull.simplices[:-2]:
                # grab convex hull edge 
                L2 = line(hull.simplices[p2], hull.simplices[p2+1])
                p2 = p2 + 1
                # see if the edge from VD and edge from CH intersect 
                R = intersection(L1, L2)
                if R:
                    # intersection means it is a candidate center for circle 
                    # find closest point by finding min distance between vertex and all points in CH 
                    for each in hull.simplices:
                        c2 = each
                        # find distance between vertex and point (radius of circle)
                        distance = math.sqrt(((each[0]-j)**2)+((each[1]-k)**2))
                        # see if it replaces any of the current 3 closest points
                        if distance<closest_point[0][0]:
                            # if distance > closest point
                            closest_point[0]=(distance,j,k)
                            if(distance>radius_max[0][0]):
                                radius_max[0]=[distance,j,k, closest_point];
                            
                          # add to list of candidates for center of circle
                        candidates.insert(p3, [R, closest_point[0]])
                    p3 = p3 + 1
                
            p = p + 1
            p2 = 0

        # print max of all min radiuses (distrance to closest point)
        # print("RADIUS MAX: ", radius_max)
        # print(closest_point)
        # print(result)
    return radius_max
