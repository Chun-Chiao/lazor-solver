
import itertools
import copy

class Block:
    def __init__(self, block_type):
        self.block_type = block_type

def get_block_interaction_edge(block, x, y, direction):
    dx, dy = direction
    if block.block_type == 'A':  # Reflect
        if x % 2 == 0:  # Horizontal edge
            return [(-dx, dy)]
        elif y % 2 == 0:  # Vertical edge
            return [(dx, -dy)]
    elif block.block_type == 'B':  # Opaque
        return []
    elif block.block_type == 'C':  # Refract
        if x % 2 == 0:  # Horizontal edge
            return [direction, (-dx, dy)]
        elif y % 2 == 0:  # Vertical edge
            return [direction, (dx, -dy)]
    return [direction]

def simulate_lazor_edge_based(grid, lazors):
    active = list(lazors)
    path = set()
    visited = set()
    height, width = len(grid), len(grid[0])

    while active:
        pos, direction = active.pop()
        key = (pos, direction)
        if key in visited:
            continue
        visited.add(key)

        while 0 <= pos[0] < width * 2 and 0 <= pos[1] < height * 2:
            path.add(pos)
            next_pos = (pos[0] + direction[0], pos[1] + direction[1])
            x, y = next_pos

            block = None
            if x % 2 == 0 and y % 2 == 1:
                bx = x // 2 - 1 if direction[0] > 0 else x // 2
                by = y // 2
            elif x % 2 == 1 and y % 2 == 0:
                bx = x // 2
                by = y // 2 - 1 if direction[1] > 0 else y // 2
            else:
                bx = by = None

            if bx is not None and 0 <= bx < width and 0 <= by < height:
                block = grid[by][bx]
                if isinstance(block, Block):
                    interactions = get_block_interaction_edge(block, x, y, direction)
                    for new_dir in interactions[1:]:
                        active.append((next_pos, new_dir))
                    if interactions:
                        direction = interactions[0]
                    else:
                        break
                    next_pos = (pos[0] + direction[0], pos[1] + direction[1])
            pos = next_pos
            visited.add((pos, direction))

    return path

def parse_bff(file_path):
    with open(file_path, 'r') as f:
        lines = [l.strip() for l in f if not l.startswith('#') and l.strip() != '']

    grid, lazors, points = [], [], []
    block_counts = {'A': 0, 'B': 0, 'C': 0}
    i = 0
    while i < len(lines):
        if lines[i] == 'GRID START':
            i += 1
            while lines[i] != 'GRID STOP':
                grid.append([None if ch == 'x' else 'o' if ch == 'o' else Block(ch) for ch in lines[i].split()])
                i += 1
        elif lines[i][0] in 'ABC':
            t, count = lines[i].split()
            block_counts[t] = int(count)
        elif lines[i][0] == 'L':
            _, x, y, dx, dy = lines[i].split()
            lazors.append(((int(x), int(y)), (int(dx), int(dy))))
        elif lines[i][0] == 'P':
            _, x, y = lines[i].split()
            points.append((int(x), int(y)))
        i += 1
    return grid, block_counts, lazors, points

def solve_edge_based(grid, block_counts, lazors, points):
    height, width = len(grid), len(grid[0])
    available = [(x, y) for y in range(height) for x in range(width) if grid[y][x] == 'o']
    blocks_to_place = ['A'] * block_counts['A'] + ['C'] * block_counts['C']

    for pos_combo in itertools.combinations(available, len(blocks_to_place)):
        for block_perm in itertools.permutations(blocks_to_place):
            temp_grid = copy.deepcopy(grid)
            for (x, y), b in zip(pos_combo, block_perm):
                temp_grid[y][x] = Block(b)
            path = simulate_lazor_edge_based(temp_grid, lazors)
            if all(p in path for p in points):
                return temp_grid
    return None


import sys
import os

def format_solution_output(grid):
    return '\n'.join(
        ' '.join('.' if x is None or x == 'o' else x.block_type for x in row)
        for row in grid
    )

def save_solution_to_file(grid, output_path="solution.txt"):
    with open(output_path, 'w') as f:
        f.write(format_solution_output(grid))

def main():
    # Define the input BFF filename here
    filename = "mad_1.bff"
    if not os.path.exists(filename):
        print(f"Error: File '{filename}' not found.")
        sys.exit(1)

    grid, block_counts, lazors, points = parse_bff(filename)
    solution = solve_edge_based(grid, block_counts, lazors, points)
    if solution:
        print("Solution found!")
        save_solution_to_file(solution)
    else:
        print("No solution found.")

# Unit test for helper function
if __name__ == "__main__":
    if 'unittest' in sys.argv:
        import unittest

        class TestLazorSolver(unittest.TestCase):
            def test_format_output(self):
                test_grid = [
                    [Block('A'), None],
                    [None, Block('C')]
                ]
                expected = "A .\n. C"
                self.assertEqual(format_solution_output(test_grid), expected)

        unittest.main(argv=['first-arg-is-ignored'], exit=False)
    else:
        main()
