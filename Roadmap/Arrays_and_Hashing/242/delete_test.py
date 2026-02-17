import unittest
from delete import Solution

class TestSol(unittest.TestCase):
  def test_sol(self):
    sol = Solution()

    self.assertEqual(sol.isAnagram('anagram', 'nagaram'), True, 'Wrong output!')
    self.assertEqual(sol.isAnagram('rat', 'car'), False, 'Wrong output!')

if __name__ == '__main__':
  unittest.main()
