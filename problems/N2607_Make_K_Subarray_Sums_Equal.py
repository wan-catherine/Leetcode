from typing import List

"""
Here we can use the gcd(length, k) to get the index diff . 
Because we need to loop the whole arr by k and n , so the correct index diff == gcd(length, k)
"""

class Solution:
    def makeSubKSumEqual(self, arr: List[int], k: int) -> int:
        length = len(arr)
        def helper(nums):
            res = 0
            if not nums:
                return res
            nums.sort()
            base = nums[len(nums) // 2]
            for n in nums:
                res += abs(n - base)
            return res
        res = 0
        visited = [0] * length
        for i in range(k):
            nums = []
            j = i
            while True:
                if visited[j]:
                    break
                visited[j] = True
                nums.append(arr[j])
                j += k
                j %= length
            res += helper(nums)
        return res
