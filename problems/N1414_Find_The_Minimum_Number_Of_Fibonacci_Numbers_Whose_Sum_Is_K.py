class Solution:
    def findMinFibonacciNumbers(self, k: int) -> int:
        nums = [1,1]
        n = 0
        while n <= k:
            n = nums[-1] + nums[-2]
            nums.append(n)

        res = 0
        for i in nums[::-1]:
            if k >= i:
                res += 1
                k -= i
            if k == 0:
                break
        return res

