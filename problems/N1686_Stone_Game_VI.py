"""
Greedy problem.
We need to sort by a+b (a is what Alice can get , b is which Bob can get).
We need to get the largest what Alice and get and also hurt the largest Bob can't get.
"""
class Solution(object):
    def stoneGameVI(self, aliceValues, bobValues):
        """
        :type aliceValues: List[int]
        :type bobValues: List[int]
        :rtype: int
        """
        length = len(aliceValues)
        values = []
        for i in range(length):
            values.append((aliceValues[i]+bobValues[i], i))
        values.sort(reverse=True)
        av, bv = 0, 0
        for i in range(length):
            if i % 2:
                bv += bobValues[values[i][1]]
            else:
                av += aliceValues[values[i][1]]
        if av > bv:
            return 1
        elif av < bv:
            return -1
        else:
            return 0
