import unittest
from delete import Solution

class TestSol(unittest.TestCase):
  def test_sol(self):
    sol = Solution()

    self.assertEqual(sol.twoSum([2, 7, 11, 15], 9), [0, 1], 'Wrong output!')
    self.assertEqual(sol.twoSum([3, 2, 4], 6), [1, 2], 'Wrong output!')
    self.assertEqual(sol.twoSum([3, 3], 6), [0, 1], 'Wrong output!')

if __name__ == '__main__':
  unittest.main()