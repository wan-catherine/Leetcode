import collections
"""
Key point : 
If a number of character is less than k, then it won't be included in the substring. 
So we can consider this character will split s into more substrings , then check those substrings
"""
class Solution(object):
    def longestSubstring(self, s, k):
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
