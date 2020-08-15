class Solution(object):
    def totalFruit(self, tree):
        """
        :type tree: List[int]
        :rtype: int
        """
        length = len(tree)
        res = 0
        start, end = 1, 1
        types = set()
        last_index = -1
        tree = tree[0:1] + tree
        while end < length + 1:
            if tree[end] in types:
                if tree[end] != tree[end-1]:
                    last_index = end
                end += 1
            else:
                if len(types) < 2:
                    types.add(tree[end])
                    last_index = end
                    end += 1
                else:
                    start = last_index
                    types = set([tree[start], tree[end]])
                    last_index = end
                    end += 1
            res = max(res, end - start)
        return res