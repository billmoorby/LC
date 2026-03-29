class Solution:

  def trap(self, height):
    if not height:
      return 0

    waterCount = 0
    n = len(height)

    left, right = 0, n-1
    maxL, maxR = height[left], height[right]

    while left < right:
      if maxL < maxR:
        left+=1
        maxL = max(maxL, height[left])
        waterCount += (maxL - height[left])
      else:
        right-=1
        maxR = max(maxR, height[right])
        waterCount += (maxR - height[right])
    
    return waterCount
