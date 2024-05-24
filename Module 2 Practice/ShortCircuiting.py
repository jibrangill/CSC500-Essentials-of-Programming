#Author Jibran Gill
#Code to learn short circuiting

#function to return if true

def function_if_true():
    print('Function True')
    return True

#funtionto return if false

def function_if_false():
    print('Function False')
    return False

def check_and_operation():
    print('EVALUATING AND OPERATION')
    print('i) function_if_true AND function_if_false')
    function_if_true() and function_if_false()
    print()
    print('ii) function_if_false AND function_if_true')
    function_if_false() and function_if_true()
    print()
    print('iii) function_if_true AND function_if_true')
    function_if_true() and function_if_true()
    print()
    print('iv) function_if_false AND function_if_fale')
    function_if_false() and function_if_false()
    print('**END**')

def check_or_operation():
    print('EVALUATING OR OPERATION')
    print('i) function_if_true OR function_if_false')
    function_if_true() or function_if_false()
    print()
    print('ii) function_if_false OR function_if_true')
    function_if_false() or function_if_true()
    print()
    print('iii) function_if_true OR function_if_true')
    function_if_true() or function_if_true()
    print()
    print('iv) function_if_false OR function_if_fale')
    function_if_false() or function_if_false()
    print('**END**')

def check_not_operation():
    print('EVALUATING NOT OPERATION')
    print('i) Not of True')
    print(not function_if_true())
    print('i) Not of False')
    print(not function_if_false())
    
## Cal the functino check_and_operation short circuting bheavior
def input_the_option():
    x = input('Enter 1 if checking AND or 2 if checking OR or 3 if checking NOT:')
    if (x == '1'):
        check_and_operation()
    elif (x == '2'):
        check_or_operation()
    elif (x == '3'):
        check_not_operation()

input_the_option()
