import unittest

import numpy as np

from Game import Game

class MyTestCase(unittest.TestCase):

    def setUp(self):
        self.g = Game()

    def test_XCol1(self):
        width,height = 3,3
        grid = np.chararray((width, height))
        grid[0] = ["X", "O", "X"]
        grid[1] = ["X", "O", "O"]
        grid[2] = ["X", "X", "O"]
        self.assertEqual("X WIN",self.g.check_win(grid))

    def test_XCol2(self):
        width,height = 3,3
        grid = np.chararray((width, height))
        grid[0] = ["X", "O", ""]
        grid[1] = ["X", "O", ""]
        grid[2] = ["X", "", ""]
        self.assertEqual("X WIN",self.g.check_win(grid))

    def test_XRow1(self):
        width,height = 3,3
        grid = np.chararray((width, height))
        grid[0] = ["X", "X", "X"]
        grid[1] = ["", "O", "O"]
        grid[2] = ["X", "", "O"]
        self.assertEqual("X WIN",self.g.check_win(grid))

    def test_XDiagonal1(self):
        width,height = 3,3
        grid = np.chararray((width, height))
        grid[0] = ["X", "O", "O"]
        grid[1] = ["O", "X", "O"]
        grid[2] = ["X", "X", "X"]
        self.assertEqual("X WIN", self.g.check_win(grid))

    def test_XDiagonal2(self):
        width,height = 3,3
        grid = np.chararray((width, height))
        grid[0] = ["X", "O", "X"]
        grid[1] = ["O", "X", "O"]
        grid[2] = ["X", "", ""]
        self.assertEqual("X WIN",self.g.check_win(grid))

    def test_XNoRes2(self):
        width,height = 3,3
        grid = np.chararray((width, height))
        grid[0] = ["", "", ""]
        grid[1] = ["", "", ""]
        grid[2] = ["", "", ""]
        self.assertEqual(None,self.g.check_win(grid))

    def test_NoRes1(self):
        width, height = 3,3
        grid = np.chararray((width, height))
        grid[0] = ["X", "O", "X"]
        grid[1] = ["O", "", "O"]
        grid[2] = ["X", "X", "O"]
        self.assertEqual(None,self.g.check_win(grid))


    def test_NoRes2(self):
        width, height = 3, 3
        grid = np.chararray((width, height))
        grid[0] = ["X", "O", "X"]
        grid[1] = ["O", "X", "O"]
        grid[2] = ["O", "X", "O"]
        self.assertEqual(None,self.g.check_win(grid))

    def test_NoRes3(self):
        width, height = 3, 3
        grid = np.chararray((width, height))
        grid[0] = ["X", "O", "O"]
        grid[1] = ["O", "X", "X"]
        grid[2] = ["X", "X", "O"]
        self.assertEqual(None,self.g.check_win(grid))

    def test_OCol1(self):
        width,height = 3,3
        grid = np.chararray((width, height))
        grid[0] = ["O", "X", "O"]
        grid[1] = ["O", "X", "X"]
        grid[2] = ["O", "O", "X"]
        self.assertEqual("O WIN",self.g.check_win(grid))

    def test_OCol2(self):
        width,height = 3,3
        grid = np.chararray((width, height))
        grid[0] = ["O", "X", ""]
        grid[1] = ["O", "X", ""]
        grid[2] = ["O", "", ""]
        self.assertEqual("O WIN",self.g.check_win(grid))

    def test_ORow1(self):
        width,height = 3,3
        grid = np.chararray((width, height))
        grid[0] = ["O", "O", "O"]
        grid[1] = ["", "X", "X"]
        grid[2] = ["O", "", "X"]
        self.assertEqual("O WIN",self.g.check_win(grid))

    def test_ODiagonal1(self):
        width,height = 3,3
        grid = np.chararray((width, height))
        grid[0] = ["O", "X", "X"]
        grid[1] = ["X", "O", "X"]
        grid[2] = ["O", "X", "O"]
        self.assertEqual("O WIN", self.g.check_win(grid))

    def test_ODiagonal2(self):
        width,height = 3,3
        grid = np.chararray((width, height))
        grid[0] = ["O", "X", "O"]
        grid[1] = ["X", "O", "X"]
        grid[2] = ["O", "X", "X"]
        self.assertEqual("O WIN",self.g.check_win(grid))

    def test_ONoRes2(self):
        width,height = 3,3
        grid = np.chararray((width, height))
        grid[0] = ["", "", ""]
        grid[1] = ["", "O", ""]
        grid[2] = ["", "", ""]
        self.assertEqual(None,self.g.check_win(grid))

    def test_NoRes1(self):
        width, height = 3,3
        grid = np.chararray((width, height))
        grid[0] = ["O", "O", "X"]
        grid[1] = ["X", "", "O"]
        grid[2] = ["X", "X", "O"]
        self.assertEqual(None,self.g.check_win(grid))


    def test_NoRes2(self):
        width, height = 3, 3
        grid = np.chararray((width, height))
        grid[0] = ["X", "O", "X"]
        grid[1] = ["O", "X", "O"]
        grid[2] = ["O", "X", "O"]
        self.assertEqual(None,self.g.check_win(grid))

    def test_NoRes3(self):
        width, height = 3, 3
        grid = np.chararray((width, height))
        grid[0] = ["X", "O", "O"]
        grid[1] = ["O", "X", "X"]
        grid[2] = ["X", "X", "O"]
        self.assertEqual(None,self.g.check_win(grid))


if __name__ == '__main__':
    unittest.main()
