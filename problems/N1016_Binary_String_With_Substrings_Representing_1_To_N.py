class Solution(object):
    def queryString(self, S, N):
        """
        :type S: str
        :type N: int
        :rtype: bool
        """
        if N == 0:
            return '0' in S
        if N == 1:
            return '1' in S

        i = 1
        while 2 ** i <= N:
            i += 1

        self.length = len(S)
        self.s = S
        if self.length < i:
            return False
        if i > 2:
            i_1 = self.helper(0, i-1, N)
            if i_1 != 2 ** (i-2):
                return False
        i_0 = self.helper(0, i, N)
        if i_0 != N - 2 ** (i-1) + 1:
            return False
        return True

    def helper(self, start, end, maximum):
        res = set()
        while end <= self.length:
            if self.s[start] == '0':
                start += 1
                end += 1
                continue
            num = int(self.s[start:end], 2)
            if num <= maximum:
                res.add(num)
            start += 1
            end += 1
        return len(res)




