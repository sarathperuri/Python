# Function for nth Fibonacci number 

def Fibonacci(n): 
	if n<0: 
		print("Incorrect input")
        elif n==0:
                return 0
	# First Fibonacci number is 0 
	elif n==1: 
		return 0
	# Second Fibonacci number is 1 
	elif n==2: 
		return 1
	else: 
		return Fibonacci(n-1)+Fibonacci(n-2) 

# Driver Program 
n = input("Enter the fibonacci number you want :")
print(Fibonacci(n)) 
