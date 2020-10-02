class Solution(object):
    def numOfBurgers(self, tomatoSlices, cheeseSlices):
        """
        :type tomatoSlices: int
        :type cheeseSlices: int
        :rtype: List[int]
        """
        if (cheeseSlices == 0 and tomatoSlices != 0) or tomatoSlices < 2 * cheeseSlices:
            return []
        jumbo = tomatoSlices - 2 * cheeseSlices
        if jumbo%2 or cheeseSlices - jumbo//2 < 0:
            return []
        return [jumbo//2 , cheeseSlices - jumbo//2]
