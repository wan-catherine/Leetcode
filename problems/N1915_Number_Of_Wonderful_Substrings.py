import collections

"""
Key point: 
status compression . 
If at some index, the status is '101', then we can check mapping[status], so between them are all even number of char. 
Then consider to change one char's even/odd, we can get the odd number.
"""

class Solution:
    def wonderfulSubstrings(self, word: str) -> int:
        mapping = collections.defaultdict(int)
        mapping[0] = 1
        status = 0
        res = 0
        for w in word:
            idx = ord(w) - ord('a')
            v = (1 << idx)
            status ^= v
            res += mapping[status]
            for i in range(10):
                val = status ^ (1 << i)
                res += mapping[val]
            mapping[status] += 1
        return res