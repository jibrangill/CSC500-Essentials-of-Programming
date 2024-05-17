#Author: Jibran Gill
#Program to add and subtract two numbers
#Part1

#function to add and subtract two numbers
def addSubtract():
    print('--Program to add and subtract two numbers enterd by user--')
    num1 = input('Enter the first number: ')
    num2 = input('Enter the second number: ')
    num1_f, num2_f = float(num1), float(num2)
    sum = num1_f + num2_f
    subt = num1_f - num2_f
    return sum, subt

#Performing a function call
result_add, result_subtract = addSubtract()

#Printint the Result
print('----------------------------')
print('RESULTS: ')
print('Sum = ',result_add)
print('Subtraction = ',result_subtract)