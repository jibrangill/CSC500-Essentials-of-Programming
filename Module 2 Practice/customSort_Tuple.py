# Author: Jibran Gill
# Program to sort a Tuple by last element

def last_element(n):
    return n[-1]

def first_element(n):
    return n[0]

def main():
    my_tuple = [(2, 12), (1, 10), (5, 11), (3, 13), (4, 14)]
    #print ('last element: ', last_element(my_tuple))
    print('Orignal Tuple: ', my_tuple)
    print ('Sorted by last element: ',sorted(my_tuple, key=last_element))
    print ('Sorted by first element: ',sorted(my_tuple, key=first_element))
if __name__ == "__main__":
    main()
