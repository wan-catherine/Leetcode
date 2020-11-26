import collections
"""
Key point : 
If a number of character is less than k, then it won't be included in the substring. 
So we can consider this character will split s into more substrings , then check those substrings
"""
class Solution(object):
    def longestSubstring_recursive(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """

        counter = collections.Counter(s)
        for c, n in counter.items():
            if n < k:
                return max(self.longestSubstring(t, k) for t in s.split(c))
        return len(s)

    """
    Use slide window.
    The key pooint is how to shrink left . 
    We check all 26 characters. 
    we check the longest substring which contains num unique characters which all those unique characters are no less than k . 
    """
    def longestSubstring(self, s, k):
        length = len(s)
        res = 0
        for num in range(1, 27):
            count = [0] * 26
            unique, no_less_than_k = 0, 0
            left, right = 0, 0
            while right < length:
                if unique <= num:
                    idx = ord(s[right]) - ord('a')
                    if count[idx] == 0:
                        unique += 1
                    count[idx] += 1
                    if count[idx] == k:
                        no_less_than_k += 1
                    right += 1
                else:
                    idx = ord(s[left]) - ord('a')
                    if count[idx] == k:
                        no_less_than_k -= 1
                    count[idx] -= 1
                    if count[idx] == 0:
                        unique -= 1
                    left += 1

                if unique == num and no_less_than_k == unique:
                    res = max(res, right - left)
        return res
