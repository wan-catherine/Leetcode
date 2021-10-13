import collections

"""
lexicographically sort we can first consider monotonic stack
"""

class Solution:
    def smallestSubsequence(self, s: str, k: int, letter: str, repetition: int) -> str:
        counter = collections.Counter(s)
        length = len(s)
        ln = counter[letter] - repetition
        ls = length - k
        stack = []
        for c in s:
            while stack and stack[-1] > c and ls > 0:
                if stack[-1] == letter:
                    if ln == 0:
                        break
                    ln -= 1
                stack.pop()
                ls -= 1
            stack.append(c)
        res = []
        for c in stack[::-1]:
            if ls > 0:
                if c == letter:
                    if ln == 0:
                        res.append(c)
                        continue
                    ln -= 1
                ls -= 1
            else:
                res.append(c)
        return "".join(res[::-1])