import unittest
import tempfile
import os
import copy

# Import your module functions and classes.
# If your code is in a single file, you can simply copy them here.
# For this example, we assume that the following names are already defined in the same module:
# Block, get_block_interaction_edge_directional, get_block_edges, print_grid,
# simulate_lazor_with_directional_logic, parse_bff, place_blocks, find_open_positions,
# check_targets_hit

###############################################################################
#                      Unit Tests for Lazors Puzzle Solver                      #
###############################################################################

class TestBlockMethods(unittest.TestCase):
    def test_repr(self):
        b = Block('A')
        self.assertEqual(repr(b), 'A')


class TestGetBlockEdges(unittest.TestCase):
    def test_edges(self):
        # For a block at grid coordinate (0, 0):
        # center_x, center_y = 0*2+1 = 1, 1, so:
        # top: (1, 0), bottom: (1, 2), left: (0, 1), right: (2, 1)
        expected = {
            'top': (1, 0),
            'bottom': (1, 2),
            'left': (0, 1),
            'right': (2, 1)
        }
        self.assertEqual(get_block_edges(0, 0), expected)


class TestBlockInteraction(unittest.TestCase):
    def test_reflective_horizontal(self):
        # For block A with horizontal edge, reflection should flip the vertical component.
        self.assertEqual(get_block_interaction_edge_directional("horizontal", "A", (1, 1)), [(1, -1)])
    
    def test_reflective_vertical(self):
        # For block A with vertical edge, reflection should flip the horizontal component.
        self.assertEqual(get_block_interaction_edge_directional("vertical", "A", (1, 1)), [(-1, 1)])
    
    def test_opaque(self):
        # For block B, the beam is absorbed (empty list).
        self.assertEqual(get_block_interaction_edge_directional("horizontal", "B", (1, -1)), [])
    
    def test_refractive_horizontal(self):
        # For block C hit on a horizontal edge, returns [direction, (dx, -dy)].
        self.assertEqual(get_block_interaction_edge_directional("horizontal", "C", (1, 1)), [(1, 1), (1, -1)])
    
    def test_refractive_vertical(self):
        self.assertEqual(get_block_interaction_edge_directional("vertical", "C", (1, 1)), [(1, 1), (-1, 1)])


class TestPlaceAndFind(unittest.TestCase):
    def setUp(self):
        # Create a simple 3x3 grid:
        # Row 0: o, o, o
        # Row 1: x, o, x    (None represents x)
        # Row 2: o, o, o
        self.grid = [
            ['o', 'o', 'o'],
            [None, 'o', None],
            ['o', 'o', 'o']
        ]
    
    def test_find_open_positions(self):
        # Expected open positions are those cells with 'o'
        expected = [(0, 0), (1, 0), (2, 0), (1, 1), (0, 2), (1, 2), (2, 2)]
        self.assertEqual(sorted(find_open_positions(self.grid)), sorted(expected))
    
    def test_place_blocks(self):
        # Place an 'A' block at (0, 0) and a 'C' block at (2, 2)
        positions = [(0, 0), (2, 2)]
        block_types = ['A', 'C']
        new_grid = place_blocks(self.grid, positions, block_types)
        self.assertTrue(isinstance(new_grid[0][0], Block))
        self.assertEqual(new_grid[0][0].block_type, 'A')
        self.assertTrue(isinstance(new_grid[2][2], Block))
        self.assertEqual(new_grid[2][2].block_type, 'C')


class TestCheckTargets(unittest.TestCase):
    def test_check_targets_hit(self):
        path = {(1, 2), (3, 4), (5, 6)}
        targets1 = [(3, 4), (1, 2)]
        targets2 = [(3, 4), (7, 8)]
        self.assertTrue(check_targets_hit(path, targets1))
        self.assertFalse(check_targets_hit(path, targets2))


class TestParseBff(unittest.TestCase):
    def test_parse_bff(self):
        # Create a sample .bff file content
        content = """\
GRID START
o o o
x o x
o o o
GRID STOP
A 1
C 2
L 0 0 1 1
P 1 1
"""
        # Write the content to a temporary file.
        with tempfile.NamedTemporaryFile(mode="w+", delete=False) as tmp:
            tmp.write(content)
            tmp_filename = tmp.name
        try:
            grid, blocks, lazors, targets = parse_bff(tmp_filename)
            self.assertEqual(len(grid), 3)
            self.assertEqual(len(grid[0]), 3)
            self.assertEqual(blocks['A'], 1)
            self.assertEqual(blocks['C'], 2)
            self.assertEqual(blocks['B'], 0)
            self.assertEqual(lazors, [((0, 0), (1, 1))])
            self.assertEqual(targets, [(1, 1)])
        finally:
            os.remove(tmp_filename)


class TestSimulation(unittest.TestCase):
    def test_simulation_simple(self):
        # Create a simple 2x2 grid with no blocks:
        grid = [
            ['o', 'o'],
            ['o', 'o']
        ]
        # One lazor starting at (0,0) moving in the direction (1,1)
        lazors = [((0, 0), (1, 1))]
        # No targets are required for this basic test of beam progression.
        path = simulate_lazor_with_directional_logic(grid, lazors)
        # The simulation area: for a grid of width=2 and height=2,
        # the coordinates are checked while 0 <= pos[0] <= 4 and 0 <= pos[1] <= 4.
        # The beam starting at (0,0) with (1,1) should travel along the diagonal.
        # Expected path: (0,0), (1,1), (2,2), (3,3), (4,4)
        expected_path = {(0, 0), (1, 1), (2, 2), (3, 3), (4, 4)}
        self.assertEqual(path, expected_path)


###############################################################################
#                             Run All Tests                                   #
###############################################################################

if __name__ == '__main__':
    unittest.main()
