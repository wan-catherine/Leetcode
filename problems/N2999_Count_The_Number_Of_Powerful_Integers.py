class Solution:
    def numberOfPowerfulInt(self, start: int, finish: int, limit: int, s: str) -> int:
        ls = len(s)
        ss, sf = str(start - 1), str(finish)

        def helper(snum):
            if len(snum) < ls:
                return 0
            return dfs(snum, 0, True)
        def dfs(snum, index, same):
            lsnum = len(snum)
            if index >= lsnum - ls:
                if not same or (snum[index:] >= s):
                    return 1
                return 0

            if same:
                res = 0
                for i in range(limit + 1):
                    if str(i) > snum[index]:
                        continue
                    if str(i) == snum[index]:
                        res += dfs(snum, index + 1, same)
                    else:
                        res += dfs(snum, index + 1, False)
                return res
            else:
                return pow(limit+1, lsnum - ls - index)

        return helper(sf) - helper(ss)