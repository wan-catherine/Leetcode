class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        indexs = []
        max = 0
        stack = []
        for index in range(0, len(s)):
            if s[index] == "(":
                stack.append(index)
            else:
                if len(stack) > 0:
                    indexs.append(stack.pop())
                    indexs.append(index)
        if len(indexs) < 2:
            return 0
        indexs.sort()
        count = 1
        for i in range(1,len(indexs)):
            if indexs[i] == indexs[i - 1] + 1:
                count += 1
            else:
                max = max if max > count else count
                count = 1
        max = max if max > count else count
        return max

