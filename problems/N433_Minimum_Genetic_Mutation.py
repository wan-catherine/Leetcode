class Solution(object):
    def minMutation(self, start, end, bank):
        """
        :type start: str
        :type end: str
        :type bank: List[str]
        :rtype: int
        """
        bank = set(bank)
        stack = [start]
        res = 0
        visited = set()
        while stack:
            new_stack = []
            for s in stack:
                if s == end:
                    return res
                for i,v in enumerate(s):
                    for j in ["A", "C", "G", "T"]:
                        if j == v:
                            continue
                        temp = "{}{}{}".format(s[:i],j,s[i+1:])
                        if temp not in bank or temp in visited:
                            continue
                        new_stack.append(temp)
                        visited.add(temp)
            res += 1
            stack = new_stack
        return -1
