class Solution:
    def addMinimum(self, word: str) -> int:
        arr = "abc"
        length = len(word)
        i, j = 0, 0
        res = 0
        while i < length:
            if arr[j] == word[i]:
                j += 1
                j %= 3
                i += 1
            else:
                res += 1
                j += 1
                j %= 3
        res += (3 - j) % 3
        return res