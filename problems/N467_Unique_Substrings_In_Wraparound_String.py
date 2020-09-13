"""
Key point:
    In order to get unique non-empty substrings's count,
    we can collection substring which ends with "a", "b", ... , "z".
    The number of substrings for str is the len(str)
"""
class Solution(object):
    def findSubstringInWraproundString_TLE(self, p):
        """
        :type p: str
        :rtype: int
        """
        if not p:
            return 0
        length = len(p)
        mapping = {}
        s = "abcdefghijklmnopqrstuvwxyz"
        for i in range(25):
            mapping[s[i]] = s[i+1]
        mapping['z'] = 'a'
        start, end = 0, 0
        res = 1
        self.visited = {p[0]}
        flag = False
        for i in range(1, length):
            if mapping[p[end]] == p[i]:
                end += 1
                flag = False
            else:
                s = p[start:end+1]
                res += self.helper(s)
                end += 1
                start = end
                flag = True
        if not flag:
            res += self.helper(p[start:end+1])
        return res

    def helper(self, s):
        count = 0
        if s in self.visited:
            return 0
        for i, c in enumerate(s):
            if s[:i+1] in self.visited:
                continue
            for j in range(i, -1, -1):
                if s[j:i+1] in self.visited:
                    continue
                count += 1
                self.visited.add(s[j:i+1])
        return count

    def findSubstringInWraproundString(self, p):
        if not p:
            return 0

        length = len(p)
        mapping = {}
        s = "abcdefghijklmnopqrstuvwxyz"
        for i in range(25):
            mapping[s[i]] = s[i + 1]
        mapping['z'] = 'a'
        previous = p[0]
        res = {key:0 for key in s}
        res[previous] = 1
        count = 1
        for i in range(1, length):
            if mapping[previous] == p[i]:
                count += 1
            else:
                count = 1
            res[p[i]] = max(res[p[i]], count)
            previous = p[i]
        return sum(res.values())
