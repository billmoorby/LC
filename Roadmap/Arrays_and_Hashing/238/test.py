import unittest
from sol import Solution

class TestSol(unittest.TestCase):
  def test_sol(self):
    sol = Solution()

    self.assertEqual(sol.productExceptSelf([1, 2, 3, 4]), [24, 12, 8, 6], 'Wrong output!')
    self.assertEqual(sol.productExceptSelf([-1, 1, 0, -3, 3]), [0, 0, 9, 0, 0], 'Wrong output!')

if __name__ == '__main__':
  unittest.main()
