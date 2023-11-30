
# importing required modules
import json
from utility import *
    
# Loading the tree of learned values.
file_path = "Reinforcement.json"
with open(file_path) as json_file:
    tree = json.load(json_file)

def game_board(state):
    '''
    Prints the game board on the screen.
    '''
    print(f'|__{state[0]}__|__{state[1]}__|__{state[2]}__|')
    print(f'|__{state[3]}__|__{state[4]}__|__{state[5]}__|')
    print(f'|__{state[6]}__|__{state[7]}__|__{state[8]}__|')
    print()

def human(player, state):
    '''
    Return new state generated after playing if game is not over otherwise 
    returns winning point.

    Parameter state: This is the state of game and must be a valid state.
    Parameter player: It is the valid player's character.
    '''
    status = is_terminal(state)     # Checking if state is terminal.
    if status[0]:
        return game_over(status[1])
    e = input('Your turn to play choose number between 1 and 9: ')
    incorrect = True
    while incorrect:        # Prompting user to enter untill he enters correct details.
        s = set_move(state, player, int(e))
        if not s:
            e = input('Please choose appropriate place: ')
        else:
            incorrect = False
    return s

def ai(state, player):
    '''
    Return new state generated after playing if game is not over otherwise 
    returns winning point.

    Parameter state: This is the state of game and must be a valid state.
    Parameter player: It is the valid player's character.
    '''
    status = is_terminal(state)     # Cheking if state is terminal.
    if status[0]:
        return game_over(status[1])
    best = -100000000000
    possible_states = []
    for i in range(9):
        if state[i] == 'N':
            possible_states.append(create_state(state, 'X', i + 1))
    for s in possible_states:      # Hunting for the value of state from tree.
        if tree[s] > best:
            state = s
            best = tree[s]
    return state

def game_over(score):
    '''
    This announce the winner of the game and other messages.

    Parameter score: This is the score secured by player.
    '''
    if score == 1:
        print('!!AI WON!!')
    elif score == -1:
        print('!! YOU WON !!')
    else:
        print('!! DRAW !!')
    print('Well played Do you wanna play again! \n')
    return 'game_over'

def main():
    '''This controlls the whole play of the game.'''
    starting_state = 'NNNNNNNNN'
    play = True
    while play:
        game_board(starting_state)
        state = human('O', starting_state)

        # checking whether game to end or restart.
        if state == 'game_over':
            i = input('Do you wanna play again? Press y for yes: ')
            if 'y' == i.lower():
                starting_state = 'NNNNNNNNN'
            else:
                play = False
        else:
            game_board(state)
            state = ai(state, 'X')

            # checking whether game to end or restart.
            if state == 'game_over':
                i = input('Do you wanna play again? Press y for yes: ')
                if 'y' == i.lower():
                    starting_state = 'NNNNNNNNN'
                else:
                    play = False
            else:
                starting_state = state


#----------------------Main-----------
if __name__ == '__main__':
    main()