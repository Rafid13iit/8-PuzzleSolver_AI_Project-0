# Entry point to run the solver and GUI

from gui import create_gui

# the initial state of the puzzle
initial_state = [
    [3, 2, 1],
    [5, 0, 4],
    [7, 6, 8]
]

if __name__ == "__main__":
    create_gui(initial_state)
