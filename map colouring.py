def is_valid_assignment(node, color, assignment, graph):
    for neighbor in graph[node]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True

def backtrack(graph, colors, assignment):
    if len(assignment) == len(graph):
        return assignment  # Solution found

    node = next(iter(set(graph.keys()) - set(assignment)))
    
    for color in colors:
        if is_valid_assignment(node, color, assignment, graph):
            assignment[node] = color
            result = backtrack(graph, colors, assignment)
            if result is not None:
                return result
            assignment.pop(node)

    return None  # No valid assignment found

def map_coloring(graph, colors):
    return backtrack(graph, colors, {})

# Example usage:
graph_example = {
    'A': ['B', 'C'],
    'B': ['A', 'C', 'D'],
    'C': ['A', 'B', 'D'],
    'D': ['B', 'C']
}

colors_example = ['Red', 'Green', 'Blue']

result = map_coloring(graph_example, colors_example)
print(result)
