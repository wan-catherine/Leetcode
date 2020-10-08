from .Utility_Tree import TreeNode
class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre:
            return None

        root = TreeNode(pre[0])
        if len(post) < 2:
            return root
        if post[-2] == pre[1]:
            root.left = self.constructFromPrePost(pre[1:], post[:-1])
            return root
        index_pre = pre.index(post[-2])
        index_post = post.index(pre[1])
        root.left = self.constructFromPrePost(pre[1:index_pre], post[:index_post+1])
        root.right = self.constructFromPrePost(pre[index_pre:], post[index_post+1:-1])
        return root