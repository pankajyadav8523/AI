def is_terminal(state):
    '''
    Return true if state is terminal otherwise False.

    Parameter state: This is string of 9 character consiting of X, O, or N only.
    '''
    i = 0
    j = 0
    while i < 9 and j < 3:
        #checking state for row-wise
        s = state[i: i+3]
        if s == 'XXX' or s == 'OOO':            
            if s == 'XXX':
                return (True, 1)
            return (True, -1)
        
        #checking state for column-wise
        s = state[j] + state[j+3] + state[j+6]
        if s == 'XXX' or s == 'OOO':
            if s == 'XXX':
                return (True, 1)
            return (True, -1)
        i += 3
        j += 1

    #checking state diagonally.
    s1 = state[0] + state[4] + state[8]
    s2 = state[2] + state[4] + state[6]
    if s1 == 'XXX' or s2 == 'XXX':
        return (True, 1)
    if s1 == 'OOO' or s2 == 'OOO':
        return (True, -1)
    
    if 'N' not in state:            # checking for draw.
        return (True, 0)
    return (False, None)            # If state is not terminal
    
def is_valid(state, position):
    '''
    Returns true if player can play at the given position otherwise False.

    Parameter state: This is the state of game and must be a valid state.
    Parameter position: This is a valid position.
    '''
    if state[position - 1] == 'N':
        return True
    False

def create_state(state, character, position):
    '''
    Creates an new state with inserting character at position in previous state.

    Parameter state: This is the state of game and must be a valid state.
    Parameter character: It is the valid player's character.
    Parameter position: This is a valid position.
    '''
    assert 1 <= position <= 9, str(position) + 'Please enter position between 1-9: '
    if is_valid(state, position):           # Checking if state is valid.
        state = state[:position - 1] + character + state[position:]
        return state
    return False

def set_move(state, character, position):
    '''
    Sets the current move.

    Parameter state: This is the state of game and must be a valid state.
    Parameter character: It is the valid player's character.
    Parameter position: This is a valid position.
    '''
    return create_state(state, character, position)