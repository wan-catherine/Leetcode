"""
YOUTOBE : https://www.youtube.com/watch?v=wUKFV55eqHE
"""
class Solution(object):
    def numMovesStonesII(self, stones):
        """
        :type stones: List[int]
        :rtype: List[int]
        """
        stones.sort()
        length = len(stones)

        if stones[1] - stones[0] > stones[-1] - stones[-2]:
            y = (stones[-2] - stones[0] + 1) - (length - 1)
        else:
            y = (stones[-1] - stones[1] + 1) - (length - 1)

        x = stones[-1]
        for i in range(length):
            j = i
            while j < length and stones[j] - stones[i] + 1 < length:
                j += 1

            if j == length:
                break

            if stones[j] - stones[i] + 1 == length:
                # m = stones[j] - stones[i] + 1 - (j - i + 1)
                m = length - (j - i + 1)
            else:
                if j - 1 - i + 1 == length - 1:
                    m = 2
                else:
                    m = length - (j -1 - i + 1)
            x = min(x, m)
        return [x, y]


