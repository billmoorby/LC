import unittest
from sol import Solution

class TestSol(unittest.TestCase):
  def test_sol(self):
    sol = Solution()

    self.assertEqual(sol.containsDuplicate([1, 2, 3, 1]), True, 'Wrong output!')
    self.assertEqual(sol.containsDuplicate([1, 2, 3, 4]), False, 'Wrong output!')
    self.assertEqual(sol.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]), True, 'Wrong output!')

if __name__ == '__main__':
  unittest.main()
