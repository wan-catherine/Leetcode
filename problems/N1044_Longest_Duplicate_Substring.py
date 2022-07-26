from functools import reduce
"""
Binary search to find the longest duplicated substring. 

Then the difficult part is how to find the duplicated substring . 
Here we use : Rabin Karp Algorithm .

Here for my solution, I use increasing way to create the has value : 
abcd = a + b*prime, c*prime*prime, d*prime*prime*prime
But it shows timeout. 

The correct way is use decreasing way :
abcd = a*prime*prime*prime + b*prime*prime + c*prime + d

The only different is how to from previous hash value to get the current hash value.
Use the decreasing way, we can simply *prime 
but for increasing way, we need to *prime**sub_len

"""

class Solution(object):
    def longestDupSubstring(self, S):
        """
        :type S: str
        :rtype: str
        """
        if not S:
            return ''
        self.S= S
        self.mod = 2**63 -1
        length = len(S)
        left, right = 0, length
        ans = ''
        s_int = [ord(c) - ord('a') for c in S]
        while left < right:
            mid = (right - left) // 2 + left
            substr = self.get_dup_substring(s_int, mid)
            if substr:
                if len(substr) > len(ans):
                    ans = substr
                left = mid + 1
            else:
                right = mid
        return ans

    def get_dup_substring_other(self, s, sub_len):
        cur_value = reduce(lambda x,y:(x*26 + y)%self.mod, s[:sub_len], 0)
        hash_str_mapping = {cur_value: [sub_len-1]}
        p = pow(26, sub_len, self.mod)
        for i in range(sub_len, len(s)):
            cur_value = (cur_value * 26 + s[i] - s[i-sub_len]*p) % self.mod
            if cur_value in hash_str_mapping:
                for end_index in hash_str_mapping[cur_value]:
                    if self.S[i-sub_len+1:i+1] == self.S[end_index-sub_len+1:end_index+1]:
                        return self.S[i-sub_len+1:i+1]
                hash_str_mapping[cur_value].append(i)
            hash_str_mapping[cur_value] = [i]

    def get_dup_substring(self, s, sub_len):
        hash_str_mapping = {}
        cur_value = None
        p = pow(26, sub_len, self.mod)
        for i in range(len(s)-sub_len+1):
            cur_value = self.get_hash_value(s, i, i+sub_len, cur_value, p)
            if cur_value in hash_str_mapping:
                for start_index in hash_str_mapping[cur_value]:
                    if self.S[i:sub_len+i] == self.S[start_index:start_index+sub_len]:
                        return self.S[i:sub_len+i]
                hash_str_mapping[cur_value].append(i)
            else:
                hash_str_mapping[cur_value] = [i]
        return ''

    def get_hash_value_(self, s, start, end, previous_value, p):
        if previous_value == None:
            cur_value = reduce(lambda x, y: (x * 26 + y) % self.mod, s[:end], 0)
        else:
            cur_value = (previous_value * 26 + s[end-1] - s[start-1] * p) % self.mod
        return cur_value

    def get_hash_value_timeout(self, s, start, end, previous_value, p):
        value = 0
        prime = 26
        if start == 0:
            k = 0
            for i in range(start, end):
                value += s[i]*prime**k
                k += 1
        else:
            # prime**(end-start-1) is a time-consuming operation
            value = (previous_value - s[start-1] + s[end-1]*p)/prime
        return value


