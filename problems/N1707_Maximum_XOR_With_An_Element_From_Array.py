import collections


class TrieNode:
    def __init__(self):
        self.one = None
        self.zero = None

class Solution(object):
    def maximizeXor(self, nums, queries):
        """
        :type nums: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        nums.sort()
        mapping = collections.defaultdict(list)
        for i, li in enumerate(queries):
            mapping[tuple(li)].append(i)
        queries.sort(key=lambda x:x[1])

        def construct_tree(n):
            node = root
            for i in range(31, -1, -1):
                temp = n & (1 << i)
                if temp:
                    if not node.one:
                        node.one = TrieNode()
                    node = node.one
                else:
                    if not node.zero:
                        node.zero = TrieNode()
                    node = node.zero

        def find_maximum_xor(n):
            node = root
            ans = 0
            for i in range(31, -1, -1):
                temp = n & (1 << i)
                if node.one and node.zero:
                    node = node.zero if temp else node.one
                    ans += 1 << i
                else:
                    if (temp == 0 and node.one) or (temp and node.zero):
                        ans += 1 << i
                    node = node.one if node.one else node.zero
            return ans

        i, length = 0, len(nums)
        res = [0] * len(queries)
        root = TrieNode()
        visited = set()
        for x, m in queries:
            if (x,m) in visited:
                continue
            visited.add((x,m))
            indexes = mapping[(x, m)]
            if nums[0] > m:
                for index in indexes:
                    res[index] = -1
                continue
            while i < length and nums[i] <= m:
                construct_tree(nums[i])
                i += 1

            val = find_maximum_xor(x)
            for index in indexes:
                res[index] = val
        return res
