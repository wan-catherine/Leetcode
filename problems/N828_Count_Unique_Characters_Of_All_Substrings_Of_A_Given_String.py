import string
"""
think about how to make a char unique in a substring. 
Let's take "XAXAXXAX" as an example, how to choose a substring which can make the second 'A' as a unique char in it?
We can take "XA(XAXX)AX" and between "()" is the substring we need . We can see here , in order to make the second 'A' unique,we need to do :
    1. insert "(" somewhere between the first and second 'A'
    2. insert ")" somewhere between the second and third 'A'
    
For #1, we can have "A(XA" and "AX(A", two ways. For #2, we have "A)XXA", "AX)XA" and "AXX)A" three ways. 
so totally we can have 2 * 3 = 6 different substring to make the second 'A' unique. s


Explanation
    1. index[26][2] record last two occurrence index for every upper characters.
    2. Initialise all values in index to -1.
    3. Loop on string S, for every character c, update its last two occurrence index to index[c].
    4. Count when loop. For example, if "A" appears twice at index 3, 6, 9 seperately, we need to count:
        For the first "A": (6-3) * (3-(-1))"
        For the second "A": (9-6) * (6-3)"
        For the third "A": (N-9) * (9-6)"
"""

class Solution(object):
    def uniqueLetterString_(self, s):
        """
        :type s: str
        :rtype: int
        """
        index = {c : [-1, -1] for c in string.ascii_uppercase}
        length = len(s)
        res = 0
        for i, v in enumerate(s):
            k, j = index[v]
            res += (i - j) * (j - k)
            index[v] = [j, i]

        # count the last time
        for v in index:
            k, j = index[v]
            res += (length - j) * (j - k)
        return res % (10**9 + 7)

    """
    DP:
    BBBBBBBBBBBBBBBBBOABCDOABCOABC
                 ^    ^   ^
                 s    f   i

    dp[i] = dp[i-1] + (i-f) - (f-s)
    """
    def uniqueLetterString(self, s):
        res, dp = 0, 0
        first, second = [-1]*26, [-1]*26
        for i, v in enumerate(s):
            index = ord(v) - ord('A')
            dp = dp + i - first[index] - (first[index] - second[index])
            res += dp
            second[index] = first[index]
            first[index] = i
        return res % (10**9 + 7)