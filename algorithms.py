# Contains BFS, DFS, IDS implementations

from collections import deque
from puzzle import generate_moves, is_goal, heuristic

def bfs(initial_state):
    """Breadth-First Search (BFS) for solving the 8-puzzle."""
    visited = set()
    queue = deque([(initial_state, [])])  # (state, path)

    while queue:
        current_state, path = queue.popleft()

        # Check if the goal has been reached
        if is_goal(current_state):
            return path

        visited.add(tuple(map(tuple, current_state)))

        # Generate next moves and add to the queue if not visited
        for next_state in generate_moves(current_state):
            if tuple(map(tuple, next_state)) not in visited:
                queue.append((next_state, path + [next_state]))

    return None

def dfs(initial_state):
    """Depth-First Search (DFS) for solving the 8-puzzle."""
    visited = set()
    stack = [(initial_state, [])]  # (state, path)

    while stack:
        current_state, path = stack.pop()

        # Check if the goal has been reached
        if is_goal(current_state):
            return path

        visited.add(tuple(map(tuple, current_state)))

        # Generate next moves and add to the stack if not visited
        for next_state in generate_moves(current_state):
            if tuple(map(tuple, next_state)) not in visited:
                stack.append((next_state, path + [next_state]))

    return None

def ids(initial_state, max_depth=50):
    """Iterative Deepening Search (IDS) for solving the 8-puzzle."""
    def dls(state, path, depth):
        """Depth-Limited Search (DLS) used within IDS."""
        if depth == 0 and is_goal(state):
            return path
        if depth > 0:
            for next_state in generate_moves(state):
                if tuple(map(tuple, next_state)) not in visited:
                    visited.add(tuple(map(tuple, next_state)))
                    result = dls(next_state, path + [next_state], depth - 1)
                    if result is not None:
                        return result
        return None

    # Try increasing depth limits until a solution is found
    for depth in range(max_depth):
        visited = set()
        result = dls(initial_state, [], depth)
        if result is not None:
            return result

    return None

def a_star(initial_state):
    """A* Search for solving the 8-puzzle using the Manhattan distance heuristic."""
    from heapq import heappop, heappush

    # Priority queue for A*, with (estimated_cost, actual_path_cost, state, path)
    priority_queue = []
    visited = set()
    heappush(priority_queue, (heuristic(initial_state), 0, initial_state, []))

    while priority_queue:
        estimated_cost, actual_cost, current_state, path = heappop(priority_queue)

        # Check if the goal has been reached
        if is_goal(current_state):
            return path

        visited.add(tuple(map(tuple, current_state)))

        # Generate next moves and add to the priority queue if not visited
        for next_state in generate_moves(current_state):
            if tuple(map(tuple, next_state)) not in visited:
                next_path = path + [next_state]
                next_cost = actual_cost + 1
                estimated_total_cost = next_cost + heuristic(next_state)
                heappush(priority_queue, (estimated_total_cost, next_cost, next_state, next_path))

    return None
