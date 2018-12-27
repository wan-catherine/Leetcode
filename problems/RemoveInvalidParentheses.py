class Solution:
    def removeInvalidParentheses(self, s):
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




