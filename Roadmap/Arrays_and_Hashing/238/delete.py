class Solution:

  def productExceptSelf(self, nums):
    res = [1] * len(nums)
    # [1, 2, 3, 4]

    # [1, 1, 2, 6]
    left_prod = 1
    for i in range(len(nums)):
      res[i] = left_prod
      left_prod *= nums[i]
    
    right_prod = 1
    for i in range(len(nums)-1, -1, -1):
      res[i] *= right_prod
      right_prod *= nums[i]
    
    return res
  