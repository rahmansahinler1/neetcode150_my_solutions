"""
You are given an m x n integer matrix matrix with the following two properties:

Each row is sorted in non-decreasing order.
The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.
"""
class Solution:
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        for row_matrix in matrix:
            l, r = 0, len(row_matrix) - 1
            while l <= r:
                m = int((l + r) / 2)
                check_value = row_matrix[m]
                if check_value < target:
                    l = m + 1
                elif check_value > target:
                    r = m - 1
                else:
                    return True
        return False
            
            
matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target = 3

matrix1 = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
target1 = 13


sol = Solution()

print(sol.searchMatrix(matrix, target))
print(sol.searchMatrix(matrix1, target1))
