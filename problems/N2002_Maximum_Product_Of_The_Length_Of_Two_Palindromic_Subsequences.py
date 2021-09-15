class Solution:
    def maxProduct_before(self, s: str) -> int:
        length = len(s)
        total = 2 ** length - 1
        memo = {}
        def check(num):
            nonlocal length
            if num in memo:
                return memo[num]
            cur = ''
            i = length - 1
            while num:
                if num & 1:
                    cur += s[i]
                num >>= 1
                i -= 1
            if cur != cur[::-1]:
                memo[num] = (False, 0)
                return False, 0
            memo[num] = (True, len(cur))
            return True, len(cur)
        res = 0
        largest = {}
        for v in range(1, total):
            f, lv = check(v)
            if not f:
                continue
            val = total - v
            if val in largest:
                res = max(res, lv * largest[val])
                continue
            state = val
            lst = 0
            while val:
                ff, lval = check(val)
                if ff:
                    lst = max(lst, lval)
                val = (val - 1) & state
            largest[val] = lst
            res = max(res, lv * lst)
        return res

    """
    Brute force to split s into two subsequence. 
    use interval DP to get the largest length of palindromic for those two subsequence. 
    Time complexity : O(2**N*N*N)
    """
    def maxProduct(self, s: str) -> int:
        length = len(s)
        total = 2 ** length - 1
        res = 0
        memo = {}
        def helper(val):
            if val in memo:
                return memo[val]
            cur = []
            for i in range(length):
                if val & (1 << i):
                    cur.append(s[i])
            l = len(cur)
            dp = [[0] * l for _ in range(l)]
            for i in range(l):
                dp[i][i] = 1
            res = 1
            for ll in range(2, l+1):
                for i in range(l - ll + 1):
                    j = i + ll - 1
                    if cur[i] == cur[j]:
                        dp[i][j] = max(dp[i][j], dp[i+1][j-1] + 2)
                    dp[i][j] = max(dp[i][j], dp[i+1][j], dp[i][j-1])
                    res = max(res, dp[i][j])
            memo[val] = res
            return res
        for v in range(1, total):
            l = helper(v)
            r = helper(total - v)
            res = max(res, l * r)
        return res