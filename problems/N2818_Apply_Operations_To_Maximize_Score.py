from typing import List

"""
Very classical problem . There are 4 keypoints : 
    1. count/find arrays by element 
    2. precompute prime_score 
    3. prev greater element / next greater element (monotonic stack)
    4. quick pow
"""
class Solution:
    def maximumScore(self, nums: List[int], k: int) -> int:
        maximum = max(nums)
        length = len(nums)
        MOL = 10 ** 9 + 7
        def getPrimeScore():
            arr = [0] * (maximum + 1)
            for i in range(2, maximum + 1):
                if arr[i] > 0:
                    continue
                j = 1
                while j*i <= maximum:
                    arr[j*i] += 1
                    j += 1
            scores = []
            for n in nums:
                scores.append(arr[n])
            return scores

        scores = getPrimeScore()
        prex = [-1] * length
        stack = []
        for i in range(length):
            while stack and scores[stack[-1]] < scores[i]:
                stack.pop()
            if stack:
                prex[i] = stack[-1]
            stack.append(i)

        suff = [length] * length
        stack = []
        for i in range(length-1, -1, -1):
            while stack and scores[stack[-1]] <= scores[i]:
                stack.pop()
            if stack:
                suff[i] = stack[-1]
            stack.append(i)

        def quickMull(x, n):
            if n == 0:
                return 1
            y = quickMull(x, n // 2) % MOL
            return (y * y % MOL) if n % 2 == 0 else (y * y % MOL * x % MOL)

        res = 1
        arr = []
        for i in range(length):
            arr.append((nums[i], (i - prex[i]) * (suff[i] - i)))
        arr.sort(key=lambda x : x[0], reverse=True)
        for n, t in arr:
            if t <= k:
                res = res * quickMull(n, t) % MOL
                k -= t
            else:
                res = res * quickMull(n, k) % MOL
                k -= k
            if k == 0:
                break
        return res % MOL





