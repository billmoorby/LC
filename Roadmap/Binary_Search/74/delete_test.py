import unittest
from delete import Solution

class TestSol(unittest.TestCase):

  def test_sol(self):
    sol = Solution()

    self.assertEqual(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 3), True, 'Wrong output!')
    self.assertEqual(sol.searchMatrix([[1, 3, 5, 7], [10, 11, 16, 20], [23, 30, 34, 60]], 13), False, 'Wrong output!')

if __name__ == '__main__':
  unittest.main()
