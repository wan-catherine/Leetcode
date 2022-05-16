class Solution:
    def countTexts(self, pressedKeys: str) -> int:
        length = len(pressedKeys)
        dp = [0] * (length + 1)
        dp[0] = 1
        for i in range(length):
            l = 3
            if pressedKeys[i] in '79':
                l = 4
            for j in range(l):
                if i - j < 0 or pressedKeys[i] != pressedKeys[i-j]:
                    break
                dp[i+1] += dp[i-j]
                dp[i + 1] %= (10 ** 9 + 7)
        return dp[-1] % (10**9 + 7)