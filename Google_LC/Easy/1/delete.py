class Solution:
  def twoSum(self, nums, target):
    dict_map = {}

    for index, num in enumerate(nums):
      diff = target - num
      if diff in dict_map:
        return [dict_map[diff], index]
      dict_map[num] = index
