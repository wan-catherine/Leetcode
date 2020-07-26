class SegmentTreeNode():
    def __init__(self, start, end, sum, left=None, right=None):
        self.start = start
        self.end = end
        self.sum = sum
        self.left = left
        self.right = right

class NumArray(object):
    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        if not nums:
            return
        length = len(nums)
        self.root = self.build_segment_tree(0, length-1, nums)

    def build_segment_tree(self, start, end, nums):
        if start == end:
            return SegmentTreeNode(start, end, nums[start])

        mid = (end - start) // 2 + start
        left = self.build_segment_tree(start, mid, nums)
        right = self.build_segment_tree(mid + 1, end, nums)
        return SegmentTreeNode(start, end, left.sum + right.sum, left, right)

    def update(self, i, val):
        """
        :type i: int
        :type val: int
        :rtype: None
        """
        self.update_segment_tree(self.root, i, val)

    def update_segment_tree(self, tree_node, i, val):
        if tree_node.start == tree_node.end == i:
            tree_node.sum = val
            return
        mid = (tree_node.end - tree_node.start) // 2 + tree_node.start
        if i <= mid:
            self.update_segment_tree(tree_node.left, i, val)
        else:
            self.update_segment_tree(tree_node.right, i, val)
        tree_node.sum = tree_node.left.sum + tree_node.right.sum

    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.get_segment_tree_sum_range(self.root, i, j)

    def get_segment_tree_sum_range(self, tree_node, i, j):
        if tree_node.start == i and tree_node.end == j:
            return tree_node.sum

        mid = (tree_node.end - tree_node.start) // 2 + tree_node.start
        if j <= mid:
            return self.get_segment_tree_sum_range(tree_node.left, i, j)
        elif i > mid:
            return self.get_segment_tree_sum_range(tree_node.right, i, j)
        else:
            return self.get_segment_tree_sum_range(tree_node.left, i, mid) + self.get_segment_tree_sum_range(tree_node.right, mid+1, j)

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)