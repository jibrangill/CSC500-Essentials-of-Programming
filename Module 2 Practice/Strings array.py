# Author: Jibran Gill
# Practicing with arrays
#Senario-2: Using numpy to create an array of strings for students enrolled in CSC500 course
#importing the array module

import numpy

def search_student(students_enrolled_arr):
    search_key = input('Enter the student name to search: ')
    is_enrolled = numpy.any(students_enrolled_arr == search_key) 
    if is_enrolled:
        print(search_key, 'is enrolled in CSC500')
    else:
        print(search_key, 'is not enrolled in CSC500')

def main():
    #creating an array of strings for the students enrolled in CSC500-1
    students_enrolled_arr = numpy.array(['Jibran', 'Neel', 'Thiang', 'Shehryar', 'Brady'], dtype='U')

    #Check the total size of class
    size_of_class = len(students_enrolled_arr)
    print('The total students in CS500 class are:',size_of_class)
    search_student(students_enrolled_arr)
if __name__ == "__main__":
    main()