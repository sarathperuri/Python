def factorial(n):
    return 1 if (n==1 or n==0) else n * factorial(n-1);
num = input("Enter the number for factorial:")
print("Factorial of {0} is {1}" .format(num,factorial(num)))

