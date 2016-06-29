#Fibonacci sequence for Nth number in iterative way
def fibonacci(n):  
    fib_prev_2 = 0 
    fib_prev_1 = 1 
    if n <= 1: 
        return 1
    for i in range(2,n+1):
        fib = fib_prev_2 + fib_prev_1 
        fib_prev_2 = fib_prev_1 
        fib_prev_1 = fib 
    return fib 

n = input('Enter n:  ') 
print "Fibonacci number at nth place is: ", fibonacci(n)