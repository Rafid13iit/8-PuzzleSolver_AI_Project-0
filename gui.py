# Handles the GUI with Tkinter

import tkinter as tk
from tkinter import messagebox
from algorithms import bfs  # Uncomment other algorithms as needed
# from algorithms import dfs, ids, a_star
from puzzle import generate_moves, GOAL_STATE, is_solvable

def create_gui(initial_state):
    window = tk.Tk()
    window.title("8-Puzzle Solver")
    window.geometry("400x500")
    window.config(bg="#f0f0f0")

    labels = [[tk.Label(window, text="", width=4, height=2, borderwidth=2, relief="solid", font=("Arial", 24), bg="white")
               for _ in range(3)] for _ in range(3)]

    # Place the labels on the grid
    for i in range(3):
        for j in range(3):
            labels[i][j].grid(row=i, column=j, padx=5, pady=5)

    def update_grid(state):
        """Update the labels to reflect the current state."""
        for i in range(3):
            for j in range(3):
                labels[i][j]["text"] = str(state[i][j]) if state[i][j] != 0 else ""
                labels[i][j]["bg"] = "#ffffff" if state[i][j] != 0 else "#cccccc"

    def solve(algorithm):
        """Run the selected algorithm and display the solution."""
        if not is_solvable(initial_state):
            messagebox.showinfo("Result", "This puzzle configuration is not solvable.")
            return

        if algorithm == 'bfs':
            solution_path = bfs(initial_state)
        # Uncomment and use other algorithms as needed
        # elif algorithm == 'dfs':
        #     solution_path = dfs(initial_state)
        # elif algorithm == 'ids':
        #     solution_path = ids(initial_state)
        # elif algorithm == 'a_star':
        #     solution_path = a_star(initial_state)
        else:
            solution_path = None

        if solution_path:
            for state in solution_path:
                update_grid(state)
                window.update()
                window.after(500)  # Delay for visualization

            messagebox.showinfo("Result", f"Puzzle solved in {len(solution_path) - 1} moves.")
        else:
            messagebox.showinfo("Result", "No solution found.")

    # Update the initial grid display
    update_grid(initial_state)

    # Buttons for selecting algorithms
    tk.Button(window, text="Solve with BFS", command=lambda: solve('bfs'), font=("Arial", 14), bg="#4caf50", fg="white").grid(row=3, column=0, columnspan=3, pady=10)
    # Uncomment these to use other algorithms
    # tk.Button(window, text="Solve with DFS", command=lambda: solve('dfs'), font=("Arial", 14), bg="#2196f3", fg="white").grid(row=4, column=0, columnspan=3, pady=10)
    # tk.Button(window, text="Solve with IDS", command=lambda: solve('ids'), font=("Arial", 14), bg="#ff5722", fg="white").grid(row=5, column=0, columnspan=3, pady=10)
    # tk.Button(window, text="Solve with A*", command=lambda: solve('a_star'), font=("Arial", 14), bg="#9c27b0", fg="white").grid(row=6, column=0, columnspan=3, pady=10)

    window.mainloop()
