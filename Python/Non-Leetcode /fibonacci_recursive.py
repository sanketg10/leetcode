#Fibonacci sequence for Nth number in recursive way
def fibonacci(n):  
    if n <= 1: 
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)

n = input('Enter n:  ') 
print "Fibonacci number at nth place is: ", fibonacci(n)