import collections


class Solution:
    def countOfAtoms(self, formula: str) -> str:
        stack = []
        parents = []
        i, length = 0, len(formula)
        while i < length:
            if formula[i].isupper():
                j = i + 1
                while j < length and formula[j].islower():
                    j += 1
                name = formula[i:j]
                num = 0
                while j < length and formula[j].isdigit():
                    num *= 10
                    num += int(formula[j])
                    j += 1
                num += (1 if num == 0 else 0)
                i = j
                stack.append([name, num])
            elif formula[i] == '(':
                parents.append(len(stack))
                i += 1
            elif formula[i] == ')':
                i += 1
                num = 0
                while i < length and formula[i].isdigit():
                    num *= 10
                    num += int(formula[i])
                    i += 1
                if num == 0:
                    num += 1
                index = parents.pop()
                for k in range(index, len(stack)):
                    stack[k][1] *= num
        mapping = collections.defaultdict(int)
        for nam, num in stack:
            mapping[nam] += num
        res = ""
        keys = sorted(mapping.keys())
        for name in keys:
            num = mapping[name]
            res += name + (str(num) if num > 1 else '')
        return res
