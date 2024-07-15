class Solution:
    def minimumOperationsToMakeEqual(self, x: int, y: int) -> int:
            if x == y:
                return 0
            if x < y:
                return y - x
            stack = {x}
            res = 0
            while stack:
                ns = set()
                for i in stack:
                    if i == y:
                        return res
                    if i % 11 == 0:
                        ns.add(i // 11)
                    if i % 5 == 0:
                        ns.add(i // 5)
                    if i >= 1:
                        ns.add(i - 1)
                    if i < 2 * x - y:
                        ns.add(i + 1)
                res += 1
                stack = ns
