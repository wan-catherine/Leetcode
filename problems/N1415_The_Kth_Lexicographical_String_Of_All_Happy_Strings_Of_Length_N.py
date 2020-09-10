class Solution(object):
    def getHappyString_dfs(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.k = k
        maximum = 3 * 2 ** (n-1)
        if k > maximum:
            return ""
        res = []
        self.dfs(n, [''], res)
        return res[k-1]

    def dfs(self, n, current, res):
        if len(current) == n + 1:
            res.append(''.join(current))
            return
        for c in 'abc':
            if c == current[-1]:
                continue
            current.append(c)
            self.dfs(n, current[:], res)
            current.pop()

    def getHappyString(self, n: int, k: int) -> str:
        def generate(prev):
            if len(prev) == n:
                yield prev
                return
            for c in 'abc':
                if not prev or c != prev[-1]:
                    yield from generate(prev + c)

        for i, res in enumerate(generate(''), 1):
            if i == k:
                return res
        return ''