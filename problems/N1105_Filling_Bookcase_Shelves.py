import sys
"""
dp[i] : the minimum height after putting ith (1-index) on the bookcase
then we need to find j which is the first book on the same level as i . 
So dp[i] = min(dp[j-1] + max(height from j to i))
"""

class Solution(object):
    def minHeightShelves(self, books, shelf_width):
        """
        :type books: List[List[int]]
        :type shelf_width: int
        :rtype: int
        """
        books = [[0,0]] + books
        length = len(books)
        dp = [sys.maxsize] * length
        dp[0] = 0

        for i in range(1, length):
            width = 0
            max_height = 0
            for j in range(i,0,-1):
                max_height = max(max_height, books[j][1])
                width += books[j][0]
                if width > shelf_width:
                    break
                dp[i] = min(dp[i], dp[j-1] + max_height)
        return dp[-1]