def fib(n):
    if (n<0):
        print("Invalid input")
    elif(n==0):
        return 0
    elif (n==1):
        return 1
    return fib(n-1)+fib(n-2)
print(fib(7))
        
