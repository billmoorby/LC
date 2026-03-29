class Solution:

  def searchMatrix(self, matrix, target):
    topRow = 0
    bottomRow = len(matrix)-1

    while topRow <= bottomRow:
      # Find row
      middleRow = (topRow + bottomRow)//2

      if target < matrix[middleRow][0]:
        bottomRow = middleRow-1
      elif target > matrix[middleRow][-1]:
        topRow = middleRow+1
      else:
        # target is within the range of the current middle row.
        break
    

    # If we break out of the loop, check if the middle row is valid. If not, we can return False.
    if not (topRow <= bottomRow):
      # No valid row found.
      return False
    
    # Found middle row.
    selectedRow = matrix[middleRow]
    left = 0
    right = len(selectedRow)-1

    while left <= right:
      mid = (left+right)//2

      if selectedRow[mid] == target:
        return True
      elif selectedRow[mid] > target:
        right = mid-1
      else:
        left = mid+1
    
    return False
  