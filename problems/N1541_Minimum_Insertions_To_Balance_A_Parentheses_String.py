"""

There are two cases here:
first : ')'
    so we have one ')' => needed_right -= 1
    if needed_right < 0 which means we have more ')' than what we need, so we need add one more '(':
    added_parentheses += 1 (add '(')
    needed_right += 2  (one '(' match two ')')

second: '('
    we need to consider if needed_right is odd which means we have some '(' match only one ')', so we need to add one more ')':
    added_parentheses += 1 (add ')')
    needed_right -= 1  (because we add one ')', so the needed_right reduce one . Here is actually the key point.
    We need to understand the needed_right is the number of right parenthese which we need to add !!!

    Then for each '(', we need two more ')' to match: needed_right += 2

Result : added_parentheses + needed_right
"""
class Solution(object):
    def minInsertions(self, s):
        """
        :type s: str
        :rtype: int
        """
        added_parentheses, needed_right = 0, 0
        for i in s:
            if i == ')':
                needed_right -= 1
                if needed_right < 0:
                    added_parentheses += 1
                    needed_right += 2
            else:
                if needed_right % 2:
                    added_parentheses += 1
                    needed_right -= 1
                needed_right += 2
        return needed_right + added_parentheses

