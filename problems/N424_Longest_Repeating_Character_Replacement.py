"""
The key point is maintain char_count and most_char_count.
Need to remember how to calculate those two when looping all string.
"""
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
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
