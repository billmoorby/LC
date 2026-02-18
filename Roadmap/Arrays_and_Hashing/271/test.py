import unittest
from sol import Solution

class TestSol(unittest.TestCase):
  def setUp(self):
    self.sol = Solution()

  def testBasicCase(self):
    strs = ["lint", "code", "love", "you"]
    encoded = self.sol.encode(strs)
    decoded = self.sol.decode(encoded)
    self.assertEqual(decoded, strs)
  
  def emptyStrings(self):
    strs = ["", "", ""]
    encoded = self.sol.encode(strs)
    decoded = self.sol.decode(encoded)
    self.assertEqual(decoded, strs)
  
  def specialCharactersTest(self):
    strs = ["hello#", "world##", "#hashtag"]
    encoded = self.sol.encode(strs)
    decoded = self.sol.decode(encoded)
    self.assertEqual(decoded, strs)

  def numbersTest(self):
    strs = ["123", "4567", "890"]
    encoded = self.sol.encode(strs)
    decoded = self.sol.decode(encoded)
    self.assertEqual(decoded, strs)

  def singleStringTest(self):
    strs = ["onlyone"]
    encoded = self.sol.encode(strs)
    decoded = self.sol.decode(encoded)
    self.assertEqual(decoded, strs)

if __name__ == '__main__':
  unittest.main()
