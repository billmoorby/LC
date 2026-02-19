import unittest
from delete import Solution

class TestSol(unittest.TestCase):

  def test_sol(self):
    sol = Solution()

    self.assertEqual(sol.isPalindrome('A man, a plan, a canal: Panama'), True, 'Wrong output!')
    self.assertEqual(sol.isPalindrome('race a car'), False, 'Wrong output!')
    self.assertEqual(sol.isPalindrome(' '), True, 'Wrong output!')

if __name__ == '__main__':
  unittest.main()
