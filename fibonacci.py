def Fibonacci(n):
   
    #if input is 0 then it will print incorrect input
    if n < 0:
        print("Incorrect input")
 
    # if n is 0 then it will return 0
    elif n == 0:
        return 0
 
    # if n is 1,2 it will return 1
    elif n == 1 or n == 2:
        return 1
 
    else:
        return Fibonacci(n-1) + Fibonacci(n-2)
 
n = int(input("Enter Number :" ))
print(Fibonacci(n))
