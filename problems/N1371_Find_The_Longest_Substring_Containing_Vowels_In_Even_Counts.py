"""
Prefix, status compression, hashtable

key point:
for i, j+1 (index of s), if we know s[i:j+1] is the substring which contains vowels in even,
which means s[:j+1] and s[:i] have same odd/even for containing vowels:
     s[:j+1] and s[:i] both contain vowels in odd
     s[:j+1] and s[:i] both contain vowels in even
=> then s[:j+1] - s[:i] = s[i:j+1] is the one .

Use hashmap to save the key - earliest index of s 
"""
class Solution(object):
    def findTheLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        length = len(s)
        index_mapping = {0:-1}
        count = [0] * 5

        res = 0
        for i in range(length):
            if s[i] == 'a':
                count[0] += 1
            elif s[i] == 'e':
                count[1] += 1
            elif s[i] == 'i':
                count[2] += 1
            elif s[i] == 'o':
                count[3] += 1
            elif s[i] == 'u':
                count[4] += 1
            key = self.covert_key(count)
            if key in index_mapping:
                res = max(res, i - index_mapping[key])
            else:
                index_mapping[key] = i
        return res

    # status compression
    def covert_key(self, count):
        key = 0
        for i in range(5):
            if count[i] % 2:
                key += 2**i # (1 << i)
        return key

