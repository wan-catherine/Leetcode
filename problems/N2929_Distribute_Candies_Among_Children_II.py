import math


class Solution:
    def distributeCandies(self, n: int, limit: int) -> int:
        # stars and bars method https://brilliant.org/wiki/integer-equations-star-and-bars/
        def ways(num):
            if num < 0:
                return 0
            return math.comb(num + 2, 2)
        if n > 3 * limit:
            return 0
        limitPlusOne = limit + 1
        oneChildExceedsLimit = ways(n - limitPlusOne)
        twoChildrenExceedLimit = ways(n - 2 * limitPlusOne)
        threeChildrenExceedLimit = ways(n - 3 * limitPlusOne)
        # Principle of Inclusion-Exclusion (PIE)
        return ways(n) - 3 * oneChildExceedsLimit + 3 * twoChildrenExceedLimit - 3 * threeChildrenExceedLimit