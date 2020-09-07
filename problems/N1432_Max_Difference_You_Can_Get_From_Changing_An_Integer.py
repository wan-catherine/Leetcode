class Solution(object):
    def maxDiff(self, num):
        """
        :type num: int
        :rtype: int
        """
        s = list(str(num))
        for i, c in enumerate(s):
            if c != '9':
                break
        maximum = 0
        for n in s:
            if n != c:
                maximum = maximum*10 + int(n)
            else:
                maximum = maximum*10 + 9

        for i, c in enumerate(s):
            if c > '1':
                break
        if i == 0 or (i == len(s) - 1 and s[i] == '1'):
            replace = 1
        else:
            replace = 0
        minimum = 0
        for n in s:
            if n != c:
                minimum = minimum * 10 + int(n)
            else:
                minimum = minimum *10 + replace
        return maximum - minimum