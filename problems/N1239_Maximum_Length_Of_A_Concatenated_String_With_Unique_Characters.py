class Solution(object):
    def maxLength_tle(self, arr):
        """
        :type arr: List[str]
        :rtype: int
        """
        self.arr = []
        for s in arr:
            if len(s) != len(set(s)):
                continue
            mask = 0
            for c in s:
                mask |= 1 << (ord(c) - ord('a'))
            self.arr.append(mask)
        self.length = len(self.arr)
        self.res = 0
        self.dfs(0, 0)
        return self.res

    def dfs(self, pos, mask):
        # self.res = max(self.res, bin(mask).count('1'))
        for i in range(pos, self.length):
            if not mask & self.arr[i]:
                self.dfs(pos+1, mask|self.arr[i])

        self.res = max(self.res, bin(mask).count('1'))

    def maxLength(self, arr) -> int:
        uniqELements = ['']
        maximum = 0
        for i in range(len(arr)):
            sz = len(uniqELements)
            for j in range(sz):
                x = arr[i] + uniqELements[j]
                if (len(x) == len(set(x))):
                    uniqELements.append(x)
                    maximum = max(maximum, len(x))
        print(uniqELements)
        return maximum
