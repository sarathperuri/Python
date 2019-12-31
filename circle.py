# Python program to find Area of a circle 

def findArea(r): 
	PI = 3.142
	return PI * (r*r); 

# Driver method 
r = input("Enter the radius:")
a = findArea(r)
print("Area is {0}".format(a)); 
 
