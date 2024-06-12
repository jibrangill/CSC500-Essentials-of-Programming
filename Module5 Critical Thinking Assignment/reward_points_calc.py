#Author: Jibran Gill
#Books Purchase Reward Point Calculator

#I am using procedural approach for this assignment
#Function to calculate the reward point
def calculate_reward_points(num_books):
    points = 0

    # Calculate points for sets of 8 books
    points += (num_books // 8) * 60
    num_books %= 8

    # Calculate points for sets of 6 books
    points += (num_books // 6) * 30
    num_books %= 6

    # Calculate points for sets of 4 books
    points += (num_books // 4) * 15
    num_books %= 4

    # Calculate points for sets of 2 books
    points += (num_books // 2) * 5
    num_books %= 2

    # If there are any remaining books, they don't contribute to points
    return points

#Program main
def main():
    check_condition = 'y'
    while check_condition == 'y' or check_condition == 'Y':
        num_books = int(input("Enter the number of books purchased this month: "))
        points = calculate_reward_points(num_books)
        print()
        print(f'Books purchased: {num_books}')
        print(f'Points awarded: {points}')
        print()
        check_condition = input('Enter y to continue or any n to exit: ')
        print()
        if check_condition == 'n' or check_condition == 'N':
            print('Good Bye!')
            break
        elif check_condition != 'y':
            print('[ERROR]Invalid Entry. Terminating Program.')

#Calling main
if __name__ == "__main__":
    main()