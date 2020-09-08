class Solution(object):
    def maxDepthAfterSplit(self, seq):
        """
        :type seq: str
        :rtype: List[int]
        """
        maximum,current = 0, 0
        stack = []
        length = len(seq)
        res = [0]*length
        for i, v in enumerate(seq):
            if v == '(':
                stack.append(v)
                current += 1
                maximum = max(maximum, current)
            else:
                stack.pop()
                current -= 1

        val = maximum // 2 + 1
        stack, current = [], 0
        for i, v in enumerate(seq):
            if v == '(':
                stack.append(v)
                current += 1
                if current >= val:
                    res[i] = 1
            else:
                stack.pop()
                if current >= val:
                    res[i] = 1
                current -= 1

        return res

