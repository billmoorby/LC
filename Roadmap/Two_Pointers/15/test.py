import unittest
from sol import Solution

class TestSol(unittest.TestCase):

  def test_sol(self):
    sol = Solution()

    self.assertEqual(sol.threeSum([-1, 0, 1, 2, -1, -4]), [[-1, -1, 2], [-1, 0, 1]], 'Wrong output!')
    self.assertEqual(sol.threeSum([0, 1, 1]), [], 'Wrong output!')
    self.assertEqual(sol.threeSum([0, 0, 0]), [[0, 0, 0]], 'Wrong output!')

if __name__ == '__main__':
  unittest.main()
