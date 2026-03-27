import unittest
from sol import Solution

class TestSol(unittest.TestCase):

  def test_sol(self):
    sol = Solution()

    self.assertEqual(sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]), 6, 'Wrong output!')
    self.assertEqual(sol.trap([4, 2, 0, 3, 2, 5]), 9, 'Wrong output!')

if __name__ == '__main__':
  unittest.main()
