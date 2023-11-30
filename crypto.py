from itertools import permutations

def solve_crypto_arithmetic(puzzle):
    unique_letters = set("".join(puzzle))  # Get unique letters from the puzzle
    for perm in permutations(range(10), len(unique_letters)):
        mapping = dict(zip(unique_letters, perm))
        if all(mapping[word[0]] != 0 for word in puzzle):  # Check for leading zeros
            num1 = int("".join(str(mapping[ch]) for ch in puzzle[0]))
            num2 = int("".join(str(mapping[ch]) for ch in puzzle[1]))
            result = int("".join(str(mapping[ch]) for ch in puzzle[2]))
            if num1 + num2 == result:  # Check if the equation is satisfied
                return mapping
    return None

# Example usage
puzzle = ("SEND", "MORE", "MONEY")
solution = solve_crypto_arithmetic(puzzle)
if solution:
    print("Solution found:")
    for word in puzzle:
        for ch in word:
            print(solution[ch], end=" ")
        print()
else:
    print("No solution found.")

