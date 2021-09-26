class Solution:
    def numDecodings(self, s: str) -> int:
        s = '#' + s
        length = len(s)
        dp = [0] * length
        dp[0] = 1
        for i in range(1, length):
            if s[i].isdigit():
                v = int(s[i])
                if v != 0:
                    dp[i] += dp[i-1]

                if s[i-1].isdigit():
                    vv = int(s[i-1:i+1])
                    if 10 <= vv <= 26:
                        dp[i] += dp[i-2]
                elif s[i-1] == '*':
                    if v <= 6:
                        dp[i] += dp[i-2] * 2
                    else:
                        dp[i] += dp[i-2]
            else:
                dp[i] += dp[i-1] * 9
                if s[i-1].isdigit():
                    if s[i-1] == '1':
                        dp[i] += dp[i-2] * 9  # 11 ~ 19
                    elif s[i-1] == '2':
                        dp[i] += dp[i-2] * 6 # 21 ~ 26
                elif s[i-1] == '*':
                    dp[i] += dp[i-2] * 15 # 11 ~ 19, 21 ~ 26
            dp[i] %= (10**9+7)
        return dp[-1]

    """
    Update at 20210926
    need to mod for each dp[i] or it will be TLE
    """
    def numDecodings(self, s: str) -> int:
        M = (10 ** 9 + 7)
        if s.startswith('0'):
            return 0
        length = len(s)
        dp = [0] * (length + 1)
        dp[0] = 1
        dp[1] = 1
        if s[0] == '*':
            dp[1] = 9
        for i in range(1, length):
            if s[i] != '*':
                v = int(s[i])
                if v == 0 and s[i - 1] in '03456789':
                    return 0
                if s[i - 1] == '*':
                    dp[i + 1] = dp[i - 1]
                    if v <= 6:
                        dp[i + 1] += dp[i - 1]
                    if v != 0:
                        dp[i + 1] += dp[i]
                elif s[i - 1] == '1':
                    if v != 0:
                        dp[i + 1] = dp[i]
                    dp[i + 1] += dp[i - 1]
                elif s[i - 1] == '2':
                    if v != 0:
                        dp[i + 1] = dp[i]
                    if v <= 6:
                        dp[i + 1] += dp[i - 1]
                else:
                    dp[i + 1] = dp[i]
            else:
                if s[i - 1] == '*':
                    dp[i + 1] += 9 * dp[i - 1] + 6 * dp[i - 1] + 9 * dp[i]
                    dp[i + 1] = dp[i + 1] % M
                    continue
                dp[i + 1] = 9 * dp[i]
                if s[i - 1] == '1':
                    dp[i + 1] += 9 * dp[i - 1]
                elif s[i - 1] == '2':
                    dp[i + 1] += 6 * dp[i - 1]
            dp[i + 1] = dp[i + 1] % M
        return dp[-1] % M


