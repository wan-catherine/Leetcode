class Solution:
    def countVowelPermutation(self, n: int) -> int:
        dpa, dpe, dpi, dpo, dpu = [0] * (n + 1), [0] * (n + 1), [0] * (n + 1), [0] * (n + 1), [0] * (n + 1)
        dpa[1], dpe[1], dpi[1], dpo[1], dpu[1] = 1, 1, 1, 1, 1
        for j in range(2, n + 1):
            dpa[j] = dpe[j-1] + dpi[j-1] + dpu[j-1]
            dpe[j] = dpa[j-1] + dpi[j-1]
            dpi[j] = dpe[j-1] + dpo[j-1]
            dpo[j] = dpi[j-1]
            dpu[j] = dpi[j-1] + dpo[j-1]
        return (dpa[-1] + dpe[-1] + dpi[-1] + dpo[-1] + dpu[-1]) % (10**9+7)
