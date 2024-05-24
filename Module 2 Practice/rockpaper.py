# Author: Jibran Gill
# Rock paper scissors game
# 2 players simulation
import random

#Funtion to randomly select item from list
def select_random(tuple_):
    random_item = random.choice(tuple_)
    return random_item

#Function to check the winner
def check_winner(player1, player2):
    if player1 == player2:
        return "It's a tie!"
    elif player1 == 'Rock':
        if player2 == 'Scissors':
            return 'Player1 wins!'
        else:
            return 'Player2 wins!'
    elif player1 == 'Scissors':
        if player2 == 'Paper':
            return 'Player1 wins!'
        else:
            return 'Player2 wins!'
    elif player1 == 'Paper':
        if player2 == 'Rock':
            return 'Player1 wins!'
        else:
            return 'Player2 2 wins!'

## My main function
def main():
    game = ('Rock', 'Paper', 'Scissors')
    print('\nRock, Paper, Scissors...\nShoot...\n')
    player1 = select_random(game)
    player2 = select_random(game)
    winner_result = check_winner(player1, player2)
    print ('Player1 got: ', player1)
    print ('Player2 got: ', player2)
    print ('Rock beats scissors, scissors beat paper and paper beats rock')
    print ('\nGame Result:', winner_result, 'Congratulations!!\n')

if __name__ == "__main__":
    main()

