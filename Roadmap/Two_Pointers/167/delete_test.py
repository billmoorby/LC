import unittest
from delete import Solution

class TestSol(unittest.TestCase):

  def test_sol(self):
    sol = Solution()

    self.assertEqual(sol.twoSum([2, 7, 11, 15], 9), [1, 2], 'Wrong output!')
    self.assertEqual(sol.twoSum([2, 3, 4], 6), [1, 3], 'Wrong output!')
    self.assertEqual(sol.twoSum([-1, 0], -1), [1, 2], 'Wrong output!')

if __name__ == '__main__':
  unittest.main()