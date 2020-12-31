import collections


class TrieNode:
    def __init__(self):
        self.one = None
        self.zero = None


class Trie:
    def __init__(self):
        self.root = {}

    def insert(self, n):
        d = self.root
        for i in range(31, -1, -1):
            if n & (1 << i):
                if 1 not in d:
                    d[1] = {}
                d = d[1]
            else:
                if 0 not in d:
                    d[0] = {}
                d = d[0]

    def xor(self, n):
        res = 0
        d = self.root
        for i in range(31, -1, -1):
            cur = n & (1 << i)
            if cur:
                if 0 in d:
                    res += (1 << i)
                    d = d[0]
                else:
                    d = d[1]
            elif cur == 0:
                if 1 in d:
                    res += (1 << i)
                    d = d[1]
                else:
                    d = d[0]
        return res

class Solution(object):
    def maximizeXor(self, nums, queries):
        nums.sort()
        mapping = collections.defaultdict(list)
        for i, li in enumerate(queries):
            mapping[tuple(li)].append(i)
        length = len(queries)
        res = [0] * length
        queries = sorted(mapping.keys(), key=lambda x: x[1])
        i, lnums = 0, len(nums)
        trie = Trie()
        for x, m in queries:
            if m < nums[0]:
                val = -1
            else:
                while i < lnums:
                    if nums[i] > m:
                        break
                    trie.insert(nums[i])
                    i += 1
                val = trie.xor(x)
            for index in mapping[(x, m)]:
                res[index] = val
        return res

    def maximizeXor_(self, nums, queries):
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
