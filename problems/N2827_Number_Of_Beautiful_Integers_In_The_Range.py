class Solution:
    def numberOfBeautifulIntegers(self, low: int, high: int, k: int) -> int:
        memo = {}
        def dfs(left, isSame, diff, r, num):
            if left == 0:
                if diff == 0 and r == 0:
                    return 1
                return 0
            if (left, isSame, diff, r, num) in memo:
                return memo[(left, isSame, diff, r, num)]
            length = len(num)
            res = 0
            if not isSame:
                for i in range(10):
                    ndiff = diff + (1 if i % 2 else -1)
                    nr = (r * 10 + i) % k
                    res += dfs(left-1, isSame, ndiff, nr, num)
            else:
                d = int(num[length - left])
                for i in range(d):
                    res += dfs(left-1, False, diff + (1 if i % 2 else -1), (r * 10 + i) % k, num)
                res += dfs(left-1, True, diff + (1 if d % 2  else -1), (r * 10 + d) % k, num)
            memo[(left, isSame, diff, r, num)] = res
            return res
        def helper(num):
            length = len(num)
            res = 0
            for i in range(2, length, 2):
                for j in range(1, 10):
                    res += dfs(i-1, False, (1 if j % 2 else -1), j%k, num)
            if length % 2 == 0:
                n = int(num[0])
                for i in range(1, n):
                    res += dfs(length-1, False, (1 if i % 2 else -1), i%k, num)
                res += dfs(length-1, True, (1 if n % 2 else -1), n%k, num)
            print(res)
            return res

        return helper(str(high)) - helper(str(low-1))