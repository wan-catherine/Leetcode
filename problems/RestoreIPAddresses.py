class Solution:
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s == None or len(s) < 4 or len(s) > 12:
            return []

        res = []
        nums = []
        self.helper(res, s, nums)
        return res

    def helper(self, res, s, nums):
        if len(nums) == 4 and len(s) == 0:
            res.append('.'.join(str(x) for x in nums))
            return

        if len(s) < 4 - len(nums) or len(s) > 3 *(4 - len(nums)):
            return

        for i in range(1,4):
            length = len(s)
            if length < i:
                continue
            n = int(s[:i])
            if (i != 1 and n == 0) or (n != 0 and n < 10 ** (i - 1)):
                continue
            if -1 < n < 256:
                nums.append(n)
                self.helper(res, s[i:], nums)
                nums.pop()
