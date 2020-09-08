class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        return self.helper(input)

    def helper(self, input):
        if input.isdigit():
            return [int(input)]
        res = []
        for i, c in enumerate(input):
            if c in '+-*':
                left = self.helper(input[:i])
                right = self.helper(input[i+1:])
                for j in left:
                    for k in right:
                        res.append(self.calculate(j, k, c))
        return res

    def calculate(self, i, j, op):
        if op == '+':
            return i+j
        elif op == '-':
            return i-j
        else:
            return i*j
