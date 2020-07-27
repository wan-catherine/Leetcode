import collections

from .Utility_Tree import TreeNode

class Solution(object):
    def findFrequentTreeSum(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        counter = collections.defaultdict(int)
        self.sum_of_tree(root, counter)
        if len(counter) < 1:
            return []
        sorted_counter = [(k,v) for k, v in sorted(counter.items(), key=lambda x:x[1], reverse=True)]
        res = [sorted_counter[0][0]]
        for k, v in sorted_counter[1:]:
            if v == sorted_counter[0][1]:
                res.append(k)
        return res

    def sum_of_tree(self, root, counter):
        if not root:
            return 0
        if not root.left and not root.right:
            counter[root.val] += 1
            return root.val

        res = root.val
        res += self.sum_of_tree(root.left, counter)
        res += self.sum_of_tree(root.right, counter)
        counter[res] += 1
        return res


