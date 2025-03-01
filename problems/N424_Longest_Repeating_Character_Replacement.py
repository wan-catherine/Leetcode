"""
The key point is maintain char_count and most_char_count.
Need to remember how to calculate those two when looping all string.
"""
import string


class Solution:
    def characterReplacement_before(self, s: str, k: int) -> int:
        char_count = [0] * 26
        most_char_count = 0
        length = len(s)
        start, end = 0, 0
        res = 0
        while end < length:
            char_count[ord(s[end]) - ord('A')] += 1
            cur_count = char_count[ord(s[end]) - ord('A')]
            most_char_count = max(most_char_count, cur_count)

            if end - start - most_char_count + 1 > k:
                char_count[ord(s[start]) - ord('A')] -= 1
                start += 1
            res = max(res, end - start + 1)
            end += 1
        return res

    def characterReplacement(self, s: str, k: int) -> int:
        length = len(s)
        counter = [0] * 26
        left, res = 0, 0
        for i in range(length):
            index = ord(s[i]) - ord('A')
            counter[index] += 1
            while i - left + 1 - max(counter) > k:
                counter[ord[s[left]]] -= 1
                left += 1
            res = max(res, i - left + 1)
        return res

    def characterReplacement_20250301(self, s: str, k: int) -> int:
        length = len(s)
        res = 0
        for c in string.ascii_uppercase:
            cur = k
            i, j = 0, 0
            while j < length:
                if s[j] != c:
                    cur -= 1
                while i < j and cur < 0:
                    if s[i] != c:
                        cur += 1
                    i += 1
                res = max(res, j - i + 1)
                j += 1
        return res