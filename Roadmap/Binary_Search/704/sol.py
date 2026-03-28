class Solution:

  def search(self, nums, target):
    low = 0
    high = len(nums)-1

    while low <= high:
      mid = (low + high)//2

      # Target is the middle number.
      if nums[mid] == target:
        return mid
      # Target is less than the middle number, search left half
      elif nums[mid] > target:
        high = mid-1
      # Target is greater than the middle number, search right half
      else:
        low = mid+1
    return -1
