# Writing a function for the same thing in recursive way -- awesome!
def factorial(number):
    if number <= 1:  # always have a base case: thats where it stops
        return 1
    else:
        return number * factorial(number - 1)

number = input('Enter a positive number: ')
print "Factorial is: ", factorial(number)


# #Writing a function for the same thing in iterative way
# def factorial(number):
#     factorial = 1
#     for i in range(1,number+1):
#         factorial = factorial*i
#     return factorial

# number = input('Enter a positive number: ')
# print "Factorial is: ", factorial(number)
