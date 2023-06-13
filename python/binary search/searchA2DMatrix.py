class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # logm + logn = logm*n O(log(m*n))
        # double binary search
        ROWS, COLS = len(matrix), len(matrix[0])

        firstRow, lastRow = 0, ROWS - 1

        while firstRow <= lastRow:
            midRow = lastRow + ((firstRow - lastRow) // 2)
            if target > matrix[midRow][-1]:
                firstRow = midRow + 1
            elif target < matrix[midRow][0]:
                lastRow = midRow - 1
            else:
                break

        # if not (firstRow <= lastRow):
        #     return False

        l, r = 0, COLS - 1
        while l <= r:
            mid = l + ((r - l) // 2)
            if matrix[midRow][mid] < target:
                l = mid + 1
            elif matrix[midRow][mid] > target:
                r = mid - 1
            else:
                return True
        return False

         

# inefficient solution
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    # O(mlogn)
        for row in matrix:
            l, r = 0, len(row) - 1
            while l <= r:
                mid = l + ((r - l) // 2)
                if row[mid] < target:
                    l = mid + 1
                elif row[mid] > target:
                    r = mid - 1
                else:
                    return True
        return False
      
      
