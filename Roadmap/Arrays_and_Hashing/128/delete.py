class Solution:

  def longestConsecutive(self, nums):
    if not nums:
      return 0
    
    max_streak = 0
    num_set = set(nums)

    for n in num_set:
      if (n-1) not in num_set:
        current_streak = 1

        while (n+1) in num_set:
          current_streak +=1
          n+=1
        max_streak = max(max_streak, current_streak)
      
    return max_streak
  