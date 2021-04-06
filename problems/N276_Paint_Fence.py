"""
You are painting a fence of n posts with k different colors. You must paint the posts following these rules:

Every post must be painted exactly one color.
At most one pair of adjacent fence posts can have the same color.
Given the two integers n and k, return the number of ways you can paint the fence.


Example 1:
Input: n = 3, k = 2
Output: 6
Explanation: All the possibilities are shown.
Note that painting all the posts red or all the posts green is invalid because there can only be at most one pair of adjacent posts that are the same color.

Example 2:
Input: n = 1, k = 1
Output: 1

Example 3:
Input: n = 7, k = 2
Output: 42

Constraints:
1 <= n <= 50
1 <= k <= 105
The answer is guaranteed to be in the range [0, 231 - 1] for the given n and k.


https://leetcode-cn.com/problems/paint-fence

Solution:
double status DP problems.
same : the number of painting ways which the last two positions are in same color
diff : the number of painting ways which the last two positions are in diff color

same = last diff
diff = last same * (k - 1) + last diff * (k - 1)
"""
class Solution:
    def numWays(self, n: int, k: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return k

        same, diff = k, k * (k - 1)
        for i in range(3, n+1):
            psame, pdiff = same, diff
            same = pdiff
            diff = psame * (k - 1) + pdiff * (k - 1)
        return same + diff