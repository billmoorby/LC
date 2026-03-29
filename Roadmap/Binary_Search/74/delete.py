class Solution:

  def searchMatrix(self, matrix, target):
    topRow = 0
    bottomRow = len(matrix)-1

    while topRow <= bottomRow:
      middleRow = (topRow + bottomRow)//2
      if target < matrix[middleRow][0]:
        bottomRow = middleRow-1
      elif target > matrix[middleRow][-1]:
        topRow = middleRow+1
      else:
        break
    
    if not (topRow <= bottomRow):
      return False
    
    selectedRow = matrix[middleRow]
    left = 0
    right = len(selectedRow)-1

    while left <= right:
      mid = (left + right)//2

      if selectedRow[mid] == target:
        return True
      elif selectedRow[mid] < target:
        left = mid+1
      else:
        right = mid-1
    
    return False
