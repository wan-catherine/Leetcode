class Solution(object):
    def longestPalindrome_self_slow_but_pass(self, s):
        """
        :type s: str
        :rtype: str
        """
        if s == None or len(s) <= 1 or s == s[::-1]:
            return s

        i = 1
        res = ""
        temp = ""
        while i < len(s):
            if i+1 < len(s) and s[i-1] == s[i+1]:
                temp = s[i-1:i+2]
                p = i - 2
                q = i + 2
                if s[i-1] == s[i]:
                    while p >= 0:
                        if s[p] == s[i-1]:
                            p -= 1
                        else:
                            break
                    while q < len(s):
                        if s[q] == s[i]:
                            q += 1
                        else:
                            break
                    temp= s[p+1:q]

                while p >=0 and q <len(s):
                    if s[p] == s[q]:
                        temp = s[p:q+1]
                        p -= 1
                        q += 1
                    else:
                        break
            elif s[i-1] == s[i]:
                temp = s[i-1:i+1]
                p = i-2
                q = i+1
                while p >= 0 and q < len(s):
                    if s[p] == s[q]:
                        temp = s[p:q + 1]
                        p -= 1
                        q += 1
                    else:
                        break
            res = temp if len(temp) > len(res) else res
            i += 1
        if len(res) == 0:
            return s[0]
        return res

    def longestPalindrome_before(self, s):
        if len(s) == 1 or s == s[::-1]:
            return s

        start = 0
        max_len = 1
        for i in range(1, len(s)):
            odd = s[i - max_len - 1: i + 1]
            even = s[i - max_len: i + 1]
            if i - max_len - 1 >= 0 and odd == odd[::-1]:
                start = i - max_len - 1
                max_len += 2
                continue
            if i - max_len >= 0 and even == even[::-1]:
                start = i - max_len
                max_len += 1

        return s[start: start + max_len]

    # Manacher's algorithm
    def longestPalindrome_(self, s):
        s_new = '#'.join('^{}*'.format(s)) #^ and $ signs are sentinels appended to each end to avoid bounds checking
        l, r, length = 0, -1, len(s_new)
        p = [0] * length
        index = 0
        for i in range(1, length-1):  #need to use [1,lenght-2] ro exclude '^ and *' , if we check the bounds, we can use [0, lenght-1]
            k = 0
            if i < r:
                j = r - i + l
                k = min(p[j], r - i)
            while s_new[i-k-1] == s_new[i+k+1]:
                k += 1

            p[i] = k
            if i + k > r:
                l = i - k
                r = i + k
            if p[i] > p[index]:
                index = i
        return s[(index - p[index]) // 2 : (index + p[index]) // 2]

    # 20200914 update, o(n^2)
    def longestPalindrome(self, s):
        length = len(s)
        if length == 1:
            return s
        ans = ''
        for i in range(1, length):
            r = 0
            while i - r - 1 >= 0 and i + r + 1 < length and s[i - r - 1] == s[i + r + 1]:
                r += 1

            if 2 * r + 1 > len(ans):
                ans = s[i - r:i + r + 1]
            r = 0
            if s[i] != s[i - 1]:
                continue
            while i - r - 2 >= 0 and i + r + 1 < length and s[i - r - 2] == s[i + r + 1]:
                r += 1
            if 2 * r + 2 > len(ans):
                ans = s[i - r - 1:i + r + 1]
        return ans


