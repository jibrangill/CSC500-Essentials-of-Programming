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
    return multiplication, division, num1_f, num2_f

##Calling the fucntion
resultMultiplication, resultDivision, num1, num2 = mulDiv()

#Printing the Result
print('----------------------------')
print('RESULT: ')
print('[Multiplication]: ', num1,'x',num2,' = ',resultMultiplication)
if num2 == 0:
    print('[DIVISION]: ERROR. Input Denominator is ', int(num2),'.', end=' ')
    print('Divison By Zero Exception.')
else:
    print('[Division]:       ',num1,'/',num2,' = ',round(resultDivision,2))