class Node:
    def __init__(self):
        self.next = [None]*26

class Solution(object):
    def minimumLengthEncoding_myself(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        leaves= []
        root = Node()
        for word in set(words):
            node = root
            for c in word[::-1]:
                index = ord(c) - ord('a')
                if not node.next[index]:
                    node.next[index] = Node()
                node = node.next[index]
            leaves.append((node, len(word) + 1))
        ans = 0
        for node, l in leaves:
            is_leaf = True
            for i in node.next:
                if i:
                    is_leaf = False
            if is_leaf:
                ans += l
        return ans

    def minimumLengthEncoding(self, words):
        root = dict()
        leaves = []
        for word in set(words):
            cur = root
            for c in word[::-1]:
                if c not in cur:
                    cur[c] = dict()
                cur = cur[c]
            leaves.append((cur, len(word)+1))
        return sum(li[1] for li in leaves if not len(li[0]))

