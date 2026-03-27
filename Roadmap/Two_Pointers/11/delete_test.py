import unittest
from delete import Solution

class TestSol(unittest.TestCase):

  def test_sol(self):
    sol = Solution()

    self.assertEqual(sol.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]), 49, 'Wrong output!')
    self.assertEqual(sol.maxArea([1, 1]), 1, 'Wrong output!')

if __name__ == '__main__':
  unittest.main()