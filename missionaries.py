from collections import deque

class State:
    def __init__(self, missionaries, cannibals, boat, parent=None):
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.boat = boat
        self.parent = parent  # Add the parent attribute

    def is_valid(self):
        if self.missionaries < 0 or self.cannibals < 0 or self.missionaries > 3 or self.cannibals > 3:
            return False
        if self.missionaries < self.cannibals and self.missionaries > 0:
            return False
        if 3 - self.missionaries < 3 - self.cannibals and 3 - self.missionaries > 0:
            return False
        return True

    def is_goal(self):
        return self.missionaries == 0 and self.cannibals == 0 and self.boat == 0

    def __eq__(self, other):
        return self.missionaries == other.missionaries and self.cannibals == other.cannibals and self.boat == other.boat

    def __hash__(self):
        return hash((self.missionaries, self.cannibals, self.boat))

def get_successors(state):
    successors = []
    moves = [(1, 0), (2, 0), (0, 1), (0, 2), (1, 1)]
    for m, c in moves:
        if state.boat == 1:
            successor = State(state.missionaries - m, state.cannibals - c, 0, parent=state)
        else:
            successor = State(state.missionaries + m, state.cannibals + c, 1, parent=state)
        if successor.is_valid():
            successors.append(successor)
    return successors

def breadth_first_search():
    initial_state = State(3, 3, 1)
    goal_state = State(0, 0, 0)

    frontier = deque([initial_state])
    explored = set()

    while frontier:
        current_state = frontier.popleft()

        if current_state.is_goal():
            return current_state

        explored.add(current_state)

        successors = get_successors(current_state)
        for successor in successors:
            if successor not in explored and successor not in frontier:
                frontier.append(successor)

    return None

def print_solution(solution):
    if solution is None:
        print("No solution found.")
    else:
        path = []
        while solution:
            path.append(solution)
            solution = solution.parent
        for t in reversed(path):
            print(t.missionaries, t.cannibals, t.boat)

if __name__ == "__main__":
    solution_state = breadth_first_search()
    print_solution(solution_state)
