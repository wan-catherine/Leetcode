from typing import List

class TreeNode:
    def __init__(self):
        self.count = 0
        self.zero = None
        self.one = None

class Solution:
    def countPairs(self, nums: List[int], low: int, high: int) -> int:
        def helper(root, val, th):
            cur = root
            ans = 0
            for i in range(31, -1, -1):
                if not cur:
                    break
                a = (val >> i) & 1
                b = (th >> i) & 1
                if a == b:
                    if a:
                        if cur.one:
                            ans += cur.one.count
                        if cur.zero:
                            cur = cur.zero
                        else:
                            break
                    else:
                        if cur.zero:
                            cur = cur.zero
                        else:
                            break
                else:
                    if a:
                        if cur.one:
                            cur = cur.one
                        else:
                            break
                    else:
                        if cur.zero:
                            ans += cur.zero.count
                        if cur.one:
                            cur = cur.one
                        else:
                            break
            return ans

        def insert(root, val):
            cur = root
            for i in range(31, -1, -1):
                v = (val >> i) & 1
                if v == 1:
                    if not cur.one:
                        cur.one = TreeNode()
                    cur = cur.one
                else:
                    if not cur.zero:
                        cur.zero = TreeNode()
                    cur = cur.zero
                cur.count += 1

        def count_less_than(val):
            root = TreeNode()
            ans = 0
            for i, num in enumerate(nums):
                ans += helper(root, num, val)
                insert(root, num)
            return ans

        return count_less_than(high+1) - count_less_than(low)