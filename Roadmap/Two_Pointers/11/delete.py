class Solution:

  def maxArea(self, height):
    left = 0
    right = len(height)-1
    largestArea = 0

    while left < right:
      currentArea = (right-left) * min(height[left], height[right])
      largestArea = max(largestArea, currentArea)
      if height[left]< height[right]:
        left+=1
      else:
        right-=1
    
    return largestArea
    