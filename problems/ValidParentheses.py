class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        left = []
        d = {"(":")", "{":"}", "[":"]"}

        for i in s:
            if i in "({[":
                left.append(i)
            elif len(left) > 0 and d[left[-1]] == i:
                left.pop(-1)
            else:
                return False

        if left == []:
            return True
        else:
            return False

