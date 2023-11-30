import heapq

class PuzzleNode:
    def __init__(self, state, parent=None, move=""):
        self.state = state
        self.parent = parent
        self.move = move
        self.cost = 0 if parent is None else parent.cost + 1

    def __lt__(self, other):
        return (self.cost + self.heuristic()) < (other.cost + other.heuristic())

    def __eq__(self, other):
        return self.state == other.state

    def __hash__(self):
        return hash(str(self.state))

    def is_goal(self):
        goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
        return self.state == goal_state

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def generate_children(self):
        children = []
        i, j = self.find_blank()

        # Possible moves: up, down, left, right
        moves = [(-1, 0, "Up"), (1, 0, "Down"), (0, -1, "Left"), (0, 1, "Right")]

        for di, dj, move in moves:
            new_i, new_j = i + di, j + dj

            if 0 <= new_i < 3 and 0 <= new_j < 3:
                new_state = [row.copy() for row in self.state]
                new_state[i][j], new_state[new_i][new_j] = new_state[new_i][new_j], new_state[i][j]
                children.append(PuzzleNode(new_state, parent=self, move=move))

        return children

    def heuristic(self):
        # Manhattan distance heuristic
        distance = 0
        for i in range(3):
            for j in range(3):
                value = self.state[i][j]
                if value != 0:
                    goal_i, goal_j = divmod(value - 1, 3)
                    distance += abs(i - goal_i) + abs(j - goal_j)
        return distance

def solve_puzzle(initial_state):
    initial_node = PuzzleNode(initial_state)
    open_set = [initial_node]
    closed_set = set()

    while open_set:
        current_node = heapq.heappop(open_set)

        if current_node.is_goal():
            # Reconstruct the path
            path = []
            while current_node:
                path.append((current_node.move, current_node.state))
                current_node = current_node.parent
            return reversed(path)

        closed_set.add(current_node)

        for child in current_node.generate_children():
            if child not in closed_set and child not in open_set:
                heapq.heappush(open_set, child)

    return None

def print_solution(solution):
    for move, state in solution:
        print(f"Move: {move}\n{state[0]}\n{state[1]}\n{state[2]}\n")
        print("cost=4")
        

if __name__ == "__main__":
    # Example initial state
    initial_state = [[1, 2, 3], [4, 5, 6], [0, 7, 8]]

    solution = solve_puzzle(initial_state)

    if solution:
        print_solution(solution)
    else:
        print("No solution found.")
        
