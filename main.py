# project 1
# multiplayer game to roll a dice

# allow user to roll a dice and get a number between 1 and 6
# Ask user if they wanna continue to roll the dice, roll again or stop there turn
# If they stop we take the score and add it up to some total.
# We constantly check if any players have a score that is greater than 50.
# If score is greater than 50 we end the game and tell the player that thy won.

import random

def roll_dice():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll

# players participating in the game
while True:
    players = input('Enter number of players (2 - 4): ')
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print('Players must be between 2 to 4 players.')
    else:
        print('Invalid number of players.')


max_score = 50
player_score = [0 for _ in range(players)]

while max(player_score) < max_score:
    for player_idx in range(players):
        print('\nPlayer number ', player_idx + 1, 'turn has just started!')
        print('Your total score is: ', player_score[player_idx],'\n')
        current_score = 0

        while True:
            should_roll = input('Would you like to roll? ')
            if should_roll.lower() != 'yes':
                break

            value = roll_dice()
            if value == 1:
                print('You rolled a 1, your turn is up!')
                current_score = 0
                break
            else:
                current_score += value
                print('You rolled a', value)
            print('Your score is: ', current_score)

        player_score[player_idx] += current_score
        print('Your total score is: ', player_score[player_idx])

    max_score =  max(player_score)
    winning_idx = player_score.index(max_score)
    print('Player number ', winning_idx + 1, ' is winner with score: ', max_score)    