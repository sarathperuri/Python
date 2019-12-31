val = input("Enter the number:")
# If num is divisible by any number 
# between 2 and val, it is not prime 
if val > 1: 
    for n in range(2,val): 
        if (val % n) == 0:
                print("No! it is not a prime number")
                break
    
    else: 
         print("Yes! It is a prime number") 