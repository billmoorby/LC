class Solution:

  def trap(self, height):
    waterCount = 0 
    n = len(height)

    # Arrays to store the max height to the left and right of each element.
    maxLeft = [0]*n
    maxRight = [0]*n

    # Create maxLeft array
    maxLeft[0] = height[0]
    for i in range(1, n):
      maxLeft[i] = max(maxLeft[i-1], height[i])
    
    # Create maxRight array
    maxRight[n-1] = height[n-1]
    for i in range(n-2, -1, -1):
      maxRight[i] = max(maxRight[i+1], height[i])
    
    # Trapped Water
    for k in range(n):
      waterCount += (min(maxLeft[k], maxRight[k]) - height[k])
    return waterCount
