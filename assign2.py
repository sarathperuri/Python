#*args
def adder(*num):
    sum = 0
    
    for n in num:
        sum = sum + n

    print("Sum:",sum)

adder(3,5)
adder(4,5,6,7)
adder(1,2,3,5,6)

#**kwargs

def intro(**data):
    print("\nData type of argument:",type(data))

    for key, value in data.items():
        print("{} is {}".format(key,value))

intro(Firstname="Sita", Lastname="Mrunal", Age=22, Phone=1234567890)
intro(Firstname="Ram", Lastname="Dulquer", Email="rd@nomail.com", Country="India", Age=25, Phone=9876543210)
