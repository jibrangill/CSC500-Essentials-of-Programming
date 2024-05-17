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
    difference = num1_f - num2_f
    return sum, difference, num1_f, num2_f

#Performing a function call
result_add, result_subtract, num1, num2 = addSubtract()

#Printint the Result
print('----------------------------')
print('RESULT: ')
print('i) Sum of ',num1,' and ',num2,' is ',result_add)
print('ii) Difference of ',num1,' and ',num2,' is ',result_subtract)
print()