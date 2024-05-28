# Author: Jibran Gill
# Numpy to create two matrix and multiply them

import numpy

def main():

    #Create two 3x3 matrix
    M1 = numpy.array([
        [1,2,3],
        [4,5,6],
        [6,7,8]
    ])

    M2 = numpy.array([
        [1,2,3],
        [4,5,6],
        [6,7,8]
    ])

    M3 = numpy.dot(M1,M2)
    print('Matrix Multiplication Result:\n',M3)
  
if __name__ == '__main__':
    main()