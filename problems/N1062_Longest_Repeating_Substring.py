"""
1062. Longest Repeating Substring
Given a string s, find out the length of the longest repeating substring(s). Return 0 if no repeating substring exists.

Example 1:
    Input: s = "abcd"
    Output: 0
    Explanation: There is no repeating substring.

Example 2:
    Input: s = "abbaba"
    Output: 2
    Explanation: The longest repeating substrings are "ab" and "ba", each of which occurs twice.

Example 3:
    Input: s = "aabcaabdaab"
    Output: 3
    Explanation: The longest repeating substring is "aab", which occurs 3 times.

Example 4:
    Input: s = "aaaaa"
    Output: 4
    Explanation: The longest repeating substring is "aaaa", which occurs twice.

Constraints:
    The string s consists of only lowercase English letters from 'a' - 'z'.
    1 <= s.length <= 1500

Here, s.length is 1500, which 1500*1500 = 2250000 = 2 * 10^6
1500*1500*log(1500) = 6*1^6 ==> Time complexity O(10**6) is acceptable.

we need to consider how long the substring is . loop one time
then we need to loop s to find how many times this substring shows in the s . loop two times.

Then we use binary search to dicide the length of substring .

"""
class Solution:
    def longestRepeatingSubstring(self, s: str) -> int:
        length = len(s)
        def count_substring(sub):
            index = s.index(sub)
            i = s[index+1:].find(sub)
            return True if i >= 0 else False
        def check(m):
            nonlocal length
            for i in range(length-m):
                if count_substring(s[i:i+m]):
                    return True
            return False
        l, r = 0, length
        while l < r:
            m = (r - l) // 2 + l
            if check(m):
                l = m + 1
            else:
                r = m
        return l - 1