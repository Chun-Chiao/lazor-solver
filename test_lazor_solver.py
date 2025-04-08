import unittest
from LazorProjectv3 import Block, get_block_edges, get_block_interaction_edge_directional, check_targets_hit, place_blocks, find_open_positions


class TestLazorSolver(unittest.TestCase):

    def test_block_edges(self):
        edges = get_block_edges(1, 1)
        expected = {
            'top': (3, 1),
            'bottom': (3, 3),
            'left': (1, 2),
            'right': (5, 2)
        }
        self.assertEqual(edges, expected)

    def test_block_interaction_reflect(self):
        direction = (1, 1)
        result = get_block_interaction_edge_directional('horizontal', 'A', direction)
        self.assertEqual(result, [(1, -1)])

        result = get_block_interaction_edge_directional('vertical', 'A', direction)
        self.assertEqual(result, [(-1, 1)])

    def test_block_interaction_splitter(self):
        direction = (1, 1)
        result = get_block_interaction_edge_directional('horizontal', 'C', direction)
        self.assertIn((1, 1), result)
        self.assertIn((1, -1), result)

    def test_targets_hit(self):
        path = [(1, 1), (2, 2), (3, 3)]
        targets = [(1, 1), (3, 3)]
        self.assertTrue(check_targets_hit(path, targets))

        targets = [(1, 1), (4, 4)]
        self.assertFalse(check_targets_hit(path, targets))

    def test_find_open_positions(self):
        grid = [
            ['x', 'o', 'x'],
            ['o', 'x', 'o']
        ]
        expected = [(1, 0), (0, 1), (2, 1)]
        self.assertEqual(find_open_positions(grid), expected)

    def test_place_blocks(self):
        grid = [
            ['x', 'o'],
            ['o', 'x']
        ]
        positions = [(1, 0), (0, 1)]
        types = ['A', 'C']
        new_grid = place_blocks(grid, positions, types)
        self.assertIsInstance(new_grid[0][1], Block)
        self.assertEqual(new_grid[0][1].block_type, 'A')
        self.assertEqual(new_grid[1][0].block_type, 'C')


if __name__ == '__main__':
    unittest.main()
