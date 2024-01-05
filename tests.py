import unittest
from maze import Maze

class Tests(unittest.TestCase):
    def test_maze_create_cells(self):
        num_cols = 12
        num_rows = 10
        m1 = Maze(0, 0, num_rows, num_cols, 10, 10)
        self.assertEqual(len(m1.cells),num_cols,)
        self.assertEqual(len(m1.cells[0]),num_rows,)

    def test_maze_create_cells_2(self):
        num_cols = 1
        num_rows = 1
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(len(m1.cells),num_cols,)
        self.assertEqual(len(m1.cells[0]),num_rows,)
        self.assertEqual(num_rows,num_cols)

    def test_maze_create_cells_3(self):
        num_cols = 0
        num_rows = 0
        m1 = Maze(0, 0, num_rows, num_cols, 20, 20)
        self.assertEqual(len(m1.cells),num_cols,)
        self.assertEqual(num_rows,num_cols)

if __name__ == "__main__":
    unittest.main()
