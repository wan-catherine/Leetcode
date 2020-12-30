class TreeNode:
    def __init__(self):
        self.one = None
        self.zero = None

class Solution(object):
    def findMaximumXOR_trie(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        root = self.construct_trie(nums)
        res = 0
        for n in nums:
            node = root
            ans = 0
            for i in range(31, -1, -1):
                temp = n & 1 << i
                if node.one and node.zero:
                    if temp:
                        node = node.zero
                    else:
                        node = node.one
                    ans += 1 << i
                else:
                    if (temp == 0 and node.one) or (temp != 0 and node.zero):
                        ans += 1 << i
                    node = node.one if node.one else node.zero
            res = max(res, ans)
        return res

    def construct_trie(self, nums):
        root = TreeNode()
        for n in nums:
            node = root
            for i in range(31,-1,-1):
                temp = n & 1 << i
                if temp == 0 :
                    if not node.zero:
                        node.zero = TreeNode()
                    node = node.zero
                else:
                    if not node.one:
                        node.one = TreeNode()
                    node = node.one
        return root

    """
    a^b = c ==> a^b^c^b = c^c^b ==> c^c = 0 ==> x^0 = x ==> a^c = b
    the number is between 0 ≤ num < 2**31, so we can check the bit one by one (0 ~ 31)
    Use mask, if the bit is the maximum, then we set it to 1 else 0. 
    
    The key point here is we assume there is a maximum value mask, then check num^mask is showed before, if yes , then the maximum is mask. 
    Then next increase mask by setting next bit as 1. 
    if no , then keep this bit as zero.
    """
    def findMaximumXOR(self, nums):
        mask = 0
        for i in range(31, -1, -1):
            temp = mask | 1 << i
            exist = set()
            for n in nums:
                exist.add(temp & n)
            for n in exist:
                if n ^ temp in exist:
                    mask = temp
                    break
        return mask



