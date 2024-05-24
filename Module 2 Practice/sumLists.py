# Practicing with lists
#Sum the list
# Author Jibran Gill

#Function to sum all items in the list
def sum_list(list):
    sum = 0
    for i in list:
        sum += i
    return sum

#Function to print the list items
def print_list(list):
     print('Items in your list are: ')
     for i in list:
          print(i, end=" ")
               
#Function to multiple all items in the list
def multiply_list_items(list):
    multiplication_var = 1
    for i in list:
         multiplication_var *= i
    return multiplication_var

#Function to search for the smallest and largest items in the list
def search_smallest_largest_items(list):
    largest_item = list[0]
    smallest_item = list[0]
    for x in list:
        if x > largest_item:
             largest_item = x
        if x < smallest_item:
             smallest_item = x
    return largest_item, smallest_item
          

#main block
def main():
     my_list= [2, 3, 4, 5, 6, 17]
     print_list(my_list)
     print()
     print('Length of list is: ', len(my_list))
     print('Sum of list items is: ', sum_list(my_list))
     print('Multiplication result of all items in list: ', multiply_list_items(my_list))
     max_var, min_var = search_smallest_largest_items(my_list)
     print('Largest item in list: ', max_var)
     print ('Smallest item in list: ', min_var)

if __name__ == "__main__":
     main()
     
