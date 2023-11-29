class TicTacToeNode:
    def __init__(self, state, value=0):
        self.state = state
        self.value = value
        self.children = []

def create_tic_tac_toe_tree():
    # Represents the initial state of the Tic-Tac-Toe board
    initial_state = [" " for _ in range(9)]

    # Create the root node with the initial state
    root = TicTacToeNode(initial_state)

    # Build the game tree starting from the root
    build_game_tree(root, True)

    return root

def build_game_tree(node, is_max_player_turn):
    # Check if the current state is a terminal state
    terminal_value = check_terminal_state(node.state)
    if terminal_value is not None:
        node.value = terminal_value
        return

    # Generate child states for the current state
    child_states = generate_child_states(node.state, is_max_player_turn)

    # Recursively build the tree for each child
    for child_state in child_states:
        child_node = TicTacToeNode(child_state)
        node.children.append(child_node)

        # Recursively build the tree for the child node
        build_game_tree(child_node, not is_max_player_turn)

        # Update the value of the current node based on the child's value
        if is_max_player_turn and child_node.value > node.value:
            node.value = child_node.value
        elif not is_max_player_turn and child_node.value < node.value:
            node.value = child_node.value

def check_terminal_state(state):
    # Check if the game has been won
    if check_winner(state, "X"):
        return 1
    elif check_winner(state, "O"):
        return -1

    # Check if the game is a draw
    if " " not in state:
        return 0

    # Game is not over yet
    return None

def check_winner(state, player):
    # Check rows, columns, and diagonals for a win
    winning_combinations = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
        [0, 4, 8], [2, 4, 6]              # Diagonals
    ]

    for combo in winning_combinations:
        if all(state[i] == player for i in combo):
            return True

    return False

def generate_child_states(state, is_max_player_turn):
    # Generate child states by placing "X" or "O" in empty spaces
    player_symbol = "X" if is_max_player_turn else "O"
    child_states = []

    for i in range(9):
        if state[i] == " ":
            child_state = state.copy()
            child_state[i] = player_symbol
            child_states.append(child_state)

    return child_states

# Create the Tic-Tac-Toe game tree
tic_tac_toe_tree = create_tic_tac_toe_tree()

# Print the root value
print("Root value:", tic_tac_toe_tree.value)
