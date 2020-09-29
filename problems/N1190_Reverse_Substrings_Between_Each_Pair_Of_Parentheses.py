class Solution(object):
    # remove the inner parenthesses first
    def reverseParentheses_slow(self, s):
        """
        :type s: str
        :rtype: str
        """
        stack = []
        res = []
        for i in s:
            if i.isalpha():
                res.append(i)
            elif i == '(':
                stack.append(len(res))
            else:
                index = stack.pop()
                res[index:] = res[index:][::-1]
        return ''.join(res)

    def reverseParentheses(self, s):
        pairs = {}
        stack = []
        for i, v in enumerate(s):
            if v == '(':
                stack.append(i)
            elif v == ')':
                index = stack.pop()
                pairs[i] = index
                pairs[index] = i

        res = []
        i, length, direction = 0, len(s), 1
        while i < length:
            if s[i].isalpha():
                res.append(s[i])
            else:
                i = pairs[i]
                direction = -direction
            i += direction
        return ''.join(res)




