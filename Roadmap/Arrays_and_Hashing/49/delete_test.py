import unittest
from delete import Solution

class TestSol(unittest.TestCase):

  def test_sol(self):
    sol = Solution()

    valid_outputs = [
      [["bat"], ["nat", "tan"], ["ate", "eat", "tea"]],
      [["bat"], ["nat", "tan"], ["ate", "tea", "eat"]],
      [["bat"], ["nat", "tan"], ["eat", "ate", "tea"]],
      [["bat"], ["nat", "tan"], ["eat", "tea", "ate"]],
      [["bat"], ["nat", "tan"], ["tea", "ate", "eat"]],
      [["bat"], ["nat", "tan"], ["tea", "eat", "ate"]],
      [["bat"], ["tan", "nat"], ["ate", "eat", "tea"]],
      [["bat"], ["tan", "nat"], ["ate", "tea", "eat"]],
      [["bat"], ["tan", "nat"], ["eat", "ate", "tea"]],
      [["bat"], ["tan", "nat"], ["eat", "tea", "ate"]],
      [["bat"], ["tan", "nat"], ["tea", "ate", "eat"]],
      [["bat"], ["tan", "nat"], ["tea", "eat", "ate"]],
      [["bat"], ["ate", "eat", "tea"], ["nat", "tan"]],
      [["bat"], ["ate", "eat", "tea"], ["tan", "nat"]],
      [["bat"], ["ate", "tea", "eat"], ["nat", "tan"]],
      [["bat"], ["ate", "tea", "eat"], ["tan", "nat"]],
      [["bat"], ["eat", "ate", "tea"], ["nat", "tan"]],
      [["bat"], ["eat", "ate", "tea"], ["tan", "nat"]],
      [["bat"], ["eat", "tea", "ate"], ["nat", "tan"]],
      [["bat"], ["eat", "tea", "ate"], ["tan", "nat"]],
      [["bat"], ["tea", "ate", "eat"], ["nat", "tan"]],
      [["bat"], ["tea", "ate", "eat"], ["tan", "nat"]],
      [["nat", "tan"], ["bat"], ["ate", "eat", "tea"]],
      [["nat", "tan"], ["bat"], ["ate", "tea", "eat"]],
      [["nat", "tan"], ["bat"], ["eat", "ate", "tea"]],
      [["nat", "tan"], ["bat"], ["eat", "tea", "ate"]],
      [["nat", "tan"], ["bat"], ["tea", "ate", "eat"]],
      [["nat", "tan"], ["bat"], ["tea", "eat", "ate"]],
      [["tan", "nat"], ["bat"], ["ate", "eat", "tea"]],
      [["tan", "nat"], ["bat"], ["ate", "tea", "eat"]],
      [["tan", "nat"], ["bat"], ["eat", "ate", "tea"]],
      [["tan", "nat"], ["bat"], ["eat", "tea", "ate"]],
      [["tan", "nat"], ["bat"], ["tea", "ate", "eat"]],
      [["tan", "nat"], ["bat"], ["tea", "eat", "ate"]],
      [["nat", "tan"], ["ate", "eat", "tea"], ["bat"]],
      [["nat", "tan"], ["ate", "eat", "tea"], ["bat"]],
      [["nat", "tan"], ["ate", "tea", "eat"], ["bat"]],
      [["nat", "tan"], ["ate", "tea", "eat"], ["bat"]],
      [["nat", "tan"], ["eat", "ate", "tea"], ["bat"]],
      [["nat", "tan"], ["eat", "ate", "tea"], ["bat"]],
      [["nat", "tan"], ["eat", "tea", "ate"], ["bat"]],
      [["nat", "tan"], ["eat", "tea", "ate"], ["bat"]],
      [["nat", "tan"], ["tea", "ate", "eat"], ["bat"]],
      [["nat", "tan"], ["tea", "eat", "ate"], ["bat"]],
      [["tan", "nat"], ["ate", "eat", "tea"], ["bat"]],
      [["tan", "nat"], ["ate", "eat", "tea"], ["bat"]],
      [["tan", "nat"], ["ate", "tea", "eat"], ["bat"]],
      [["tan", "nat"], ["ate", "tea", "eat"], ["bat"]],
      [["tan", "nat"], ["eat", "ate", "tea"], ["bat"]],
      [["tan", "nat"], ["eat", "ate", "tea"], ["bat"]],
      [["tan", "nat"], ["eat", "tea", "ate"], ["bat"]],
      [["tan", "nat"], ["eat", "tea", "ate"], ["bat"]],
      [["tan", "nat"], ["tea", "ate", "eat"], ["bat"]],
      [["tan", "nat"], ["tea", "eat", "ate"], ["bat"]],
      [["ate", "eat", "tea"], ["bat"], ["nat", "tan"]],
      [["ate", "eat", "tea"], ["bat"], ["tan", "nat"]],
      [["ate", "tea", "eat"], ["bat"], ["nat", "tan"]],
      [["ate", "tea", "eat"], ["bat"], ["tan", "nat"]],
      [["eat", "ate", "tea"], ["bat"], ["nat", "tan"]],
      [["eat", "ate", "tea"], ["bat"], ["tan", "nat"]],
      [["eat", "tea", "ate"], ["bat"], ["nat", "tan"]],
      [["eat", "tea", "ate"], ["bat"], ["tan", "nat"]],
      [["tea", "ate", "eat"], ["bat"], ["nat", "tan"]],
      [["tea", "ate", "eat"], ["bat"], ["tan", "nat"]],
      [["ate", "eat", "tea"], ["nat", "tan"], ["bat"]],
      [["ate", "eat", "tea"], ["tan", "nat"], ["bat"]],
      [["ate", "tea", "eat"], ["nat", "tan"], ["bat"]],
      [["ate", "tea", "eat"], ["tan", "nat"], ["bat"]],
      [["eat", "ate", "tea"], ["nat", "tan"], ["bat"]],
      [["eat", "ate", "tea"], ["tan", "nat"], ["bat"]],
      [["eat", "tea", "ate"], ["nat", "tan"], ["bat"]],
      [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]],
      [["tea", "ate", "eat"], ["nat", "tan"], ["bat"]],
      [["tea", "ate", "eat"], ["tan", "nat"], ["bat"]],
      [["tea", "eat", "ate"], ["nat", "tan"], ["bat"]],
      [["tea", "eat", "ate"], ["tan", "nat"], ["bat"]],
    ]

    self.assertIn(sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]), valid_outputs, 'Wrong output!')
    self.assertEqual(sol.groupAnagrams([""]), [[""]], 'Wrong ouput!')
    self.assertEqual(sol.groupAnagrams(["a"]), [["a"]], 'Wrong output!')


if __name__ == '__main__':
  unittest.main()
