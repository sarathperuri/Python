# python program to check if x is a perfect square 
import math 

# A utility function that returns true if x is perfect square 
def isPerfectSquare(x): 
	s = int(math.sqrt(x)) 
	return s*s == x 

# Returns true if n is a Fibinacci Number, else false 
def isFibonacci(n): 

	# n is Fibinacci if one of 5*n*n + 4 or 5*n*n - 4 or both 
	# is a perferct square 
	return isPerfectSquare(5*n*n + 4) or isPerfectSquare(5*n*n - 4) 
	
# A utility function to test above functions 
low = input("Enter the low range:")
high = input("Enter the high range:")
for i in range(low,high + 1): 
	if (isFibonacci(i) == True): 
		print i,"is a Fibonacci Number"
	else: 
		print i,"is a not Fibonacci Number "
