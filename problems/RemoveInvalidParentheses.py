from typing import List


class Solution:
    def removeInvalidParentheses_before(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        if s == None:
            return [""]

        if self.IsValid(s):
            return [s]

        l = 0
        r = 0
        for i in s:
            if i == "(":
                l += 1
            if l == 0 and i == ")":
                r += 1
            elif l > 0 and i == ")":
                l -= 1

        res = []
        self.DFS(s, 0, l, r, res)
        return res

    def IsValid(self, s):
        l = []
        for i in s:
            if i not in ["(", ")"]:
                continue
            if len(l) == 0 or i == "(":
                l.append(i)
                continue
            if i == ")" and l[-1] == "(":
                l.pop()

        return len(l) == 0

    def DFS(self, s, index, left, right, res):
        if left == 0 and right == 0:
            if self.IsValid(s):
                res.append(s)
            return

        for i in range(index, len(s)):
            if i != index and s[i] == s[i-1]:
                continue

            if s[i] == ")" or s[i] == "(":
                current = s[:i] + s[i+1:]
                if right > 0:
                    self.DFS(current, i, left, right-1, res)
                elif left > 0:
                    self.DFS(current, i, left-1, right, res)

    """
    Key point is how to remove duplidated results. 
    rules:
    1. if s[index] == cur[-1], then you must choose it 
    2. if s[index] != cur[-1], then you can choose it or you can not choose it .
    
    This way, if we have several same characters in the array, we can make sure that 
    we only choose same characters from right. 
    like ooxxxx : oox, ooxx, ooxxx, ooxxxx. 
    
    """
    def removeInvalidParentheses(self, s: str) -> List[str]:
        length = len(s)
        res = [""]

        def dfs(index, left, cur):
            nonlocal length, res
            if left < 0:
                return
            if index == length:
                if left:
                    return
                if len(res[0]) < len(cur):
                    res = [''.join(cur)]
                elif len(res[0]) == len(cur) and len(res[0]) != 0:
                    res.append(''.join(cur))
                return
            if s[index] not in '()':
                cur.append(s[index])
                dfs(index + 1, left, cur)
                return
            cur.append(s[index])
            dfs(index + 1, left + (1 if s[index] == '(' else -1), cur[:])
            cur.pop()
            if not cur or s[index] != cur[-1]:
                dfs(index + 1, left, cur[:])

        dfs(0, 0, [])
        return res




