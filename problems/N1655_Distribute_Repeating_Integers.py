import collections
"""
We have nums , first convert it to the counter . We don't really care about the key, ONLY care about the value (how many it has for same key).
So count is an array which shows different len(count) and number of each one of them.

Then we need to assign those to len(quantity) customers.
We have at most 10 customers, need to find if we can make all of them satisfied. 
1 <= m <= 10 ==> the time complexity might be 2 ** m 
==> bit mask to represent the status of all given customers satisfied or not. 

dp[i][j] : we use all i interges in count to get the status j . 
dp[len(count)][2**m-1] will be the answer. 

dp[i][j] == True , if :
    1. dp[i-1][j] == True  or 
    2.
        a. count[i] can make part of j satisfied ==> count[i] >= subset(j)
        b. dp[i-1][j - subset] = True
        
so we need to check all subset of j .
    
"""

class Solution(object):
    def canDistribute_dp(self, nums, quantity):
        """
        :type nums: List[int]
        :type quantity: List[int]
        :rtype: bool
        """
        counter = collections.Counter(nums)
        count = [0]
        for i, v in counter.items():
            count.append(v)

        m, n = len(quantity), len(count)
        dp = [[False] * (1 << m) for _ in range(n)]

        def can_satifily_subset(count, subset):
            res = 0
            for i in range(len(quantity)):
                if (subset >> i) & 1:
                    res += quantity[i]
            return count >= res

        for i in range(n):
            dp[i][0] = True

        for i in range(1, n):
            for j in range(1, 1<<m):
                if dp[i-1][j]:
                    dp[i][j] = True
                    continue
                subset = j
                while subset:
                    if dp[i-1][j - subset] and can_satifily_subset(count[i], subset):
                        dp[i][j] = True
                        break
                    subset = (subset - 1) & j
        return dp[-1][-1]



    def canDistribute(self, nums, quantity):
        arr = sorted(collections.Counter(nums).values(), reverse=True)
        quantity.sort(reverse=True)
        if quantity[0] > arr[0]:
            return False
        memo = {}
        def backtracking(index, cur):
            if (index, tuple(cur)) in memo:
                return memo[(index, tuple(cur))]
            if index == len(quantity):
                return True

            if sum(quantity[index:]) < max(cur):
                return True

            res = False
            visited = set()
            for i in range(len(cur)):
                if cur[i] >= quantity[index] :
                    # here for cur (arr), we actually have a lot of same value (for nums , there are a lot of number which have same count)
                    if cur[i] in visited:
                        print(cur[i])
                        continue
                    cur[i] -= quantity[index]
                    res |= backtracking(index+1, cur)
                    cur[i] += quantity[index]
                    visited.add(cur[i])
            memo[(index, tuple(cur))] = res
            return res

        return backtracking(0, arr)