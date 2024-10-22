# Logic for the 8-puzzle game (e.g., move generation, goal check)

import copy

# The goal state of the 8-puzzle
GOAL_STATE = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

def is_goal(state):
    """Check if the given state is the goal state."""
    return state == GOAL_STATE

def generate_moves(state):
    """
    Generate possible moves (up, down, left, right) for the empty tile (0).
    Returns a list of new states.
    """
    moves = []
    x, y = find_zero(state)

    # Define directions with their respective deltas (row, col)
    directions = {
        'up': (x - 1, y),
        'down': (x + 1, y),
        'left': (x, y - 1),
        'right': (x, y + 1)
    }

    for direction, (new_x, new_y) in directions.items():
        if 0 <= new_x < 3 and 0 <= new_y < 3:
            new_state = copy.deepcopy(state)
            # Swap the empty tile with the adjacent tile
            new_state[x][y], new_state[new_x][new_y] = new_state[new_x][new_y], new_state[x][y]
            moves.append(new_state)

    return moves

def find_zero(state):
    """Find the coordinates of the empty tile (0) in the puzzle."""
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j

def is_solvable(state):
    """
    Check if a given 8-puzzle state is solvable.
    A state is solvable if the number of inversions is even.
    """
    inversions = 0
    # Flatten the 2D puzzle into a 1D list excluding the zero (empty tile)
    flat_state = [tile for row in state for tile in row if tile != 0]

    # Count inversions
    for i in range(len(flat_state)):
        for j in range(i + 1, len(flat_state)):
            if flat_state[i] > flat_state[j]:
                inversions += 1

    return inversions % 2 == 0

def heuristic(state):
    """
    Heuristic function for A* (Manhattan distance).
    Calculates the sum of distances of each tile from its goal position.
    """
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                target_x, target_y = divmod(value - 1, 3)
                distance += abs(target_x - i) + abs(target_y - j)
    return distance
