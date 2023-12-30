from typing import List

class TrieNode:
    def __init__(self):
        self.zero = None
        self.one = None
        self.count = 0

class Solution:
    def maximumStrongPairXor(self, nums: List[int]) -> int:
        length = len(nums)
        nums.sort()
        root = TrieNode()
        def add(num):
            cur = root
            for i in range(20, -1, -1):
                if num & (1 << i) == 0:
                    if cur.zero == None:
                        cur.zero = TrieNode()
                    cur = cur.zero
                else:
                    if cur.one == None:
                        cur.one = TrieNode()
                    cur = cur.one
                cur.count += 1

        def dfs(num):
            cur = root
            ans = 0
            for i in range(20, -1, -1):
                if num & (1 << i) == 0:
                    if cur.one and cur.one.count > 0:
                        cur = cur.one
                        ans += (1 << i)
                    else:
                        cur = cur.zero
                else:
                    if cur.zero and cur.zero.count > 0:
                        cur = cur.zero
                        ans += (1 << i)
                    else:
                        cur = cur.one
            return ans

        def remove(num):
            cur = root
            for i in range(20, -1, -1):
                if num & (1 << i) == 0:
                    cur = cur.zero
                else:
                    cur = cur.one
                cur.count -= 1

        res = 0
        r = 0
        for i in range(length):
            while r < length and nums[r] <= 2 * nums[i]:
                add(nums[r])
                r += 1
            res = max(res, dfs(nums[i]))
            remove(nums[i])
        return res

