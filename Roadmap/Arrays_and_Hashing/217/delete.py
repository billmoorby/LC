class Solution:
  def containsDuplicate(self, nums):
    dict_map = {}

    for n in nums:
      if n in dict_map:
        return True
      dict_map[n] = dict_map.get(n, 0)+1
    
    return False
  