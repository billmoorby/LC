import unittest
from sol import Solution

class TestSol(unittest.TestCase):
  def test_sol(self):
    sol = Solution()

    self.assertEqual(sol.longestConsecutive([100, 4, 200, 1, 3, 2]), 4, 'Wrong output!')
    self.assertEqual(sol.longestConsecutive([0, 3, 7, 2, 5, 8, 4, 6, 0, 1]), 9, 'Wrong output!')
    self.assertEqual(sol.longestConsecutive([1, 0, 1, 2]), 3, 'Wrong output!')

if __name__ == '__main__':
  unittest.main()
