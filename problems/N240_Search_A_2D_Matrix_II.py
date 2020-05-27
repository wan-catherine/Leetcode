"""
key point is checking left corner number
if target == left corner number , then finish, return True
if target > left corner number , it means the target can only show in right of this number
so we can ignore the whole column , because the column, the left corner number is the largest

if target < left corner number , it means the target can only show in the up of this number
so we can ignore the whole row , because the row , the left corner number is the smallest

using this way , each comparison , we can get rid of one column or row , so the whole
time complexity is o(row_len * col_len)

before I read the answer , I tried to use the matrix[i][i] to compare .
this will work efficient when row_len ~= col_len.
But if row_len ~= n * col_len or n * row_len ~= col_len, then need to consider more situation.
As a result, the code will be much more . 

"""
class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or not matrix[0] or target < matrix[0][0] or target > matrix[-1][-1]:
            return False

        row_len = len(matrix)
        col_len = len(matrix[0])

        i = row_len - 1
        j = 0
        while i >= 0 and j < col_len:
            if matrix[i][j] == target:
                return True
            if matrix[i][j] > target:
                i -= 1
            else:
                j += 1
        return False