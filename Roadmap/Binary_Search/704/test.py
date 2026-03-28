import unittest
from sol import Solution

class TestSol(unittest.TestCase):

  def test_sol(self):
    sol = Solution()

    self.assertEqual(sol.search([-1, 0, 3, 5, 9, 12], 9), 4, 'Wrong output!')
    self.assertEqual(sol.search([-1, 0, 3, 5, 9, 12], 2), -1, 'Wrong output!')
    self.assertEqual(sol.search([5], 5), 0, 'Wrong output!')

if __name__ == '__main__':
  unittest.main()
