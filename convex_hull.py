#Function to find the convex hull of a given set of points using the jarvis algorithm
#References: https://www.geeksforgeeks.org/convex-hull-set-1-jarviss-algorithm-or-wrapping/

def find_convex_hull(data_array):
	#write result to this string that will print in txt file
	result=''
	data=''
	
	#obtain length of data array
	n=len(data_array)
	
	#make sure there is more than three points
	if n<3:
		return
	
	#find the leftmost point
	l=Convex_hull.left_index(data_array)
	
	#variables that are used in the loop to find the convex hull
	convex= []
	p=l
	q=0
	
	while(True):
		#add current point to the hull
		convex.append(p)	
		#keep track of the last visited, most counterclockwise point in q
		q = (p+1) % n
		for i in range(n):
			#if i is more counterclockwise than q, update it
			if(Convex_hull.orientation(data_array[p], data_array[i], data_array[q]) == 2):
				q = i	
		#since q is the most counterclockwise, set p=q so it gets added to the hull
		p=q		
		#make sure we don't return to the first point
		if(p == l):
			break
		
	#method is called just to return the data points of the convex hull
	
	for i in convex:
		print(i)	
		
	#printing results
	for points in convex:
		result= result +"("+ str(data_array[points].x)+ "," + str(data_array[points].y) + ")\n"
	for i in data_array:
		data= data + str(i) +"\n"
	
	result= "Convex Hull Results:\n\nData Points:\n" + data + "Convex Hull Data Points:\n"+ result
	
	return result

class Convex_hull:	

	#returns the leftmost point out of the data set of points
	def left_index(data_array):
		min=0
		for i in range(1,len(data_array)):
			if data_array[i].x < data_array[min].x:
				min=i
			elif data_array[i].x == data_array[min].x:
				if data_array[i].y > data_array[minn].y:
					min=i
		return min
	
	#returns the orientation of the points, 0 for collinear, 1 for clockwise, 2 for counterclockwise	
	def orientation(p,q,r):
		result= ((q.y-p.y) * (r.x-q.x)) - ((q.x-p.x) * (r.y-q.y))
		
		if result == 0:
			return 0
		elif result > 0:
			return 1
		else:
			return 2
	
	#used in pytest to test the result of the convex hull method
	#def convex_results(data_array, convex):
		
	
	
	
	
	
	
	
	
	
	
	
	

   
	