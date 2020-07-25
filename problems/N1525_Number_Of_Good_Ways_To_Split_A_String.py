class Solution:
    def numSplits(self, s: str) -> int:
        length = len(s)
        prefix_count = [[0] * 27]
        for i in range(1, length + 1):
            prefix_count.append(prefix_count[-1][:])
            prefix_count[i][ord(s[i - 1]) - ord('a')] += 1
            prefix_count[i][-1] = sum([1 for j in range(26) if prefix_count[i][j] > 0])

        res = 0
        for i in range(1, length):
            temp = 0
            for j in range(26):
                if prefix_count[i][j] == 0:
                    continue
                temp += 1 if prefix_count[-1][j] == prefix_count[i][j] else 0
            if prefix_count[-1][-1] - temp == prefix_count[i][-1]:
                res += 1
        return res