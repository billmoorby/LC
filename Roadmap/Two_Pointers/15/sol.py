class Solution:

  def threeSum(self, nums):
    newList = []
    nums.sort()

    # If the 'k' value repeats, we skip over it.
    for index, k in enumerate(nums):
      if index > 0 and k == nums[index-1]:
        continue

      left, right = index+1, len(nums)-1
      while left < right:
        tripleSum = k + nums[left] + nums[right]
        if tripleSum > 0:
          right-=1
        elif tripleSum < 0:
          left+=1
        else:
          newList.append([k, nums[left], nums[right]])
          # We update the pointers.
          # What if one or both the pointers encounters a duplicate? We shift again.
          # We just need to update one pointer. Here we're choosing left.
          left+=1
          while left < right and nums[left] == nums[left-1]:
            left+=1
    return newList
