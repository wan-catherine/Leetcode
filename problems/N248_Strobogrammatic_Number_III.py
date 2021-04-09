"""
Given two strings low and high that represent two integers low and high where low <= high,
return the number of strobogrammatic numbers in the range [low, high].
A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).

Example 1:
Input: low = "50", high = "100"
Output: 3

Example 2:
Input: low = "0", high = "0"
Output: 1

Constraints:
1 <= low.length, high.length <= 15
low and high consist of only digits.
low <= high
low and high do not contain any leading zeros except for zero itself.

https://leetcode-cn.com/problems/strobogrammatic-number-iii

0xxxx0, 1xxxx1, 8xxxx8, 6xxxx9, 9xxxx6.
xxxx: can means strobogrammatic number before . it can be even or odd.
"""
class Solution:
    def strobogrammaticInRange(self, low: str, high: str) -> int:
        pairs = [('0', '0'), ('1', '1'), ('8', '8'), ('6', '9'), ('9', '6')]
        ans = 0
        ll, lh = len(low), len(high)

        def helper(n):
            nonlocal ans, ll, lh
            if n == 0:
                return [""]
            cur_nums = []
            if n == 1:
                cur_nums = ['1', '8', '0']
            else:
                pre_nums = helper(n - 2)
                for pre in pre_nums:
                    for pair in pairs:
                        cur_nums.append(pair[0] + pre + pair[1])
            if ll <= n << lh:
                for num in cur_nums:
                    if (num == '0' or num[0] != '0') and int(low) <= int(num) <= int(high):
                        ans += 1
            return cur_nums
        helper(lh)
        helper(lh - 1)
        return ans
