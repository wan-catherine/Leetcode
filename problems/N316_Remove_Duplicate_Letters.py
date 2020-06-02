"""
monotonic stack (increasing stack)

We need to maintain two dictionary:
letter_count_mapping :
    key : letter
    value : the count of letter in the s

in_stack_mapping:
    key : letter
    value : False if letter not in stack, True if letter in stack

The reason why we need in_stack_mapping is in case we have some letter which in stack but it still > the coming one .
At this time, we shouldn't pop it. see : test_removeDuplicateLetters_7

This is a good problem, I need to recap it later.
"""

class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return s

        letter_count_mapping = {}
        in_stack_mapping = {}
        for i in s:
            count = letter_count_mapping.setdefault(i,0) + 1
            letter_count_mapping[i] = count
            in_stack_mapping[i] = False

        stack = []

        for i in s:
            if in_stack_mapping[i] and letter_count_mapping[i] > 0:
                letter_count_mapping[i] -= 1
                continue

            while stack and stack[-1] > i:
                if letter_count_mapping[stack[-1]] > 0:
                    letter = stack.pop()
                    in_stack_mapping[letter] = False
                else:
                    break
            stack.append(i)
            in_stack_mapping[i] = True
            letter_count_mapping[i] -= 1
        return ''.join(stack)



