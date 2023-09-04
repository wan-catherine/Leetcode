class Solution:
    def minimumOperations(self, num: str) -> int:
        num = num
        length = len(num)
        fzero, ffive = -1, -1
        cur = length
        for i in range(length - 1, -1, -1):
            if num[i] in ['0', '5'] and fzero != -1:
                cur = min(cur, length - i - 2)
            elif num[i] in ['2', '7'] and ffive != -1:
                cur = min(cur, length - i - 2)
            elif i == 0 and fzero != -1:
                cur = min(cur, length - 1)

            if num[i] == '0' and fzero == -1:
                fzero = i
            elif num[i] == '5' and ffive == -1:
                ffive = i
        return cur