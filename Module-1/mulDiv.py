#Author: Jibran Gill
#Program to multiple and divide two numbers
#Part2

#Function to multiply and divide twp numbers
def mulDiv():
    print('--Program to multiple and divide two numbers enterd by user--')
    num1 = input('Enter the first number: ')
    num2 = input('Enter the second number: ')
    num1_f, num2_f = float(num1), float(num2)
    multiplication = num1_f * num2_f
    try:
        division = num1_f/num2_f
    except ZeroDivisionError:
        division = "#DIV/0! error"
        print('[ERROR] Divison by zero exception occured')
    return multiplication, division

##Calling the fucntion
checkMultiplication, checkDivision = mulDiv()

#Printing the Result
print('----------------------------')
print('RESULTS: ')
print('Multiplication = ',checkMultiplication)
print('Division = ',checkDivision)