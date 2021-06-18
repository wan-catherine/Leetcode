from typing import List


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

    def maxLength_dfs(self, arr: List[str]) -> int:
        status = set()
        for word in arr:
            if len(set(word)) != len(word):
                continue
            val = 0
            for c in word:
                d = ord(c) - ord('a')
                val += (1 << d)
            status.add(val)
        status = list(status)
        # here need to append 0 in the end , to make sure it will always to run to 'index == length'
        # for test_maxLength_4
        status.append(0)
        length = len(status)
        res = 0
        def get_n(num):
            ans = 0
            while num:
                if num%2:
                    ans += 1
                num //= 2
            return ans

        def dfs(index, cur):
            nonlocal res, length
            if index == length:
                res = max(res, get_n(cur))
                return
            for i in range(index, length):
                # if we don't append 0 in the end of status, it will might skip the last one, so index == length won't execute.
                if status[i] & cur:
                    continue
                dfs(i+1, status[i] | cur)
        dfs(0, 0)
        return res
