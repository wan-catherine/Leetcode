class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        l = len(path)
        if l < 2:
            return path
        if path[l - 1] != "/":
            path += "/"
            l += 1
        a = ""
        res = []
        for i in range(1, l):
            if path[i] != "/":
                a += path[i]
            else:
                if a == "..":
                    if len(res) > 0:
                        res.pop()
                elif a == ".":
                    a = ""
                    continue
                elif a != "":
                    res.append(a)
                a = ""
        return "/" + "/".join(res)