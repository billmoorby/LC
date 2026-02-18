import unittest
from sol import Solution

class TestSol(unittest.TestCase):

  def test_sol(self):
    sol = Solution()

    valid_outputs_1 = [
      [1, 2], 
      [2, 1]
    ]

    valid_outputs_3 = [
      [1, 2], 
      [2, 1]
    ]

    self.assertIn(sol.topKFrequent([1, 1, 1, 2, 2, 3], 2), valid_outputs_1, 'Wrong output!')
    self.assertEqual(sol.topKFrequent([1], 1), [1], 'Wrong output!')
    self.assertIn(sol.topKFrequent([1, 2, 1, 2, 1, 2, 3, 1, 3, 2], 2), valid_outputs_3, 'Wrong output!')

if __name__ == '__main__':
  unittest.main() 