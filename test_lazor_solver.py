
import unittest
from LazorProjectv6_commented_full import (
    Block,
    get_block_interaction_edge_directional,
    get_block_edges,
    place_blocks,
    find_open_positions,
    check_targets_hit
)


class TestLazorSolver(unittest.TestCase):

    def test_block_reflection_A(self):
        # Reflective block - horizontal edge
        result = get_block_interaction_edge_directional('horizontal', 'A', (1, 1))
        self.assertEqual(result, [(1, -1)])

    def test_block_reflection_B(self):
        # Opaque block - absorbs lazor
        result = get_block_interaction_edge_directional('vertical', 'B', (1, 0))
        self.assertEqual(result, [])

    def test_block_reflection_C(self):
        # Refractive block - vertical edge
        result = get_block_interaction_edge_directional('vertical', 'C', (1, 0))
        self.assertIn((1, 0), result)
        self.assertIn((-1, 0), result)

    def test_get_block_edges(self):
        # Check edge coordinates for block at (1, 1)
        edges = get_block_edges(1, 1)
        expected = {
            'top': (3, 1),
            'bottom': (3, 3),
            'left': (1, 2),
            'right': (5, 2)
        }
        self.assertEqual(edges, expected)

    def test_place_blocks(self):
        grid = [['o', 'o'], ['o', 'o']]
        new_grid = place_blocks(grid, [(0, 0)], ['A'])
        self.assertIsInstance(new_grid[0][0], Block)
        self.assertEqual(new_grid[0][0].block_type, 'A')

    def test_find_open_positions(self):
        grid = [['o', 'x'], ['o', 'o']]
        positions = find_open_positions(grid)
        self.assertEqual(positions, [(0, 0), (0, 1), (1, 1)])

    def test_check_targets_hit(self):
        path = {(1, 1), (2, 2), (3, 3)}
        targets = [(1, 1), (3, 3)]
        self.assertTrue(check_targets_hit(path, targets))
        self.assertFalse(check_targets_hit(path, [(0, 0)]))


if __name__ == '__main__':
    unittest.main()
