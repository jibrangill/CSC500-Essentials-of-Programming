#Author Jibran Gill

#Defining Boolean Variables
condition1 = True
condition2 = False
condition3 = True

# Creating a boolean exmpression with and and or 
if condition1 or condition2 and condition3:
    print('Condition 1 is true, or both Condition 2 and Condition 3 are true.')
else:
    print('Neither Condition 1 is true, nor both Condition 2 and Condition 3 are true.')

#Creating a not boolean expression
if not condition2:
    print('Condition2 is false')

if not condition1:
    print('Conditon1 is false')
else:
    print('Condition1 is true')
