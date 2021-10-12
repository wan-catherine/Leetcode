import collections
from typing import List


class Solution:
    def stoneGameIX(self, stones: List[int]) -> bool:
        def win(count, total, turn):
            if sum(count.values()) == 0:
                return True if turn else False
            if count[0] > 0:
                count[0] -= 1
                if not win(count, total, 1-turn):
                    return True
            elif count[total] > 0:
                count[total] -= 1
                if not win(count, 2 * total % 3, 1-turn):
                    return True
            return False

        counter = collections.Counter([stone % 3 for stone in stones])
        temp = counter.copy()
        if temp[1] > 0:
            temp[1] -= 1
            if not win(temp, 1, 1):
                return True
        if counter[2] > 0:
            counter[2] -= 1
            if not win(counter, 2, 1):
                return True
        return False
