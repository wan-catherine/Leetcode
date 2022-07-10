from typing import List


class Solution:
    def fillCups(self, amount: List[int]) -> int:
        a, b, c = sorted(amount, reverse=True)
        if a >= b + c:
            return a
        return a + c - (a - (b - c)) // 2

    def fillCups_classical(self, amount: List[int]) -> int:
        return max(max(amount), (sum(amount) + 1) // 2)

