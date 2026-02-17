import collections

class Solution:
  def groupAnagrams(self, strs):
    word_map = collections.defaultdict(list)

    for s in strs:
      letter_binary = [0] * 26
      for char in s:
        letter_binary[ord(char) - ord('a')]+=1
      word_map[tuple(letter_binary)].append(s)
    
    return list(word_map.values())
