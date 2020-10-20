"""
for target :
1,2,3,4,5,...x,
when we get the least number which larger than target :
the diff = sum - target
if diff is even, then it means we can flip the sign of diff// 2 .
if diff is odd , then we need to add more number (x+1 or even x+2 ) until we can get even diff.  
"""
class Solution(object):
    def reachNumber(self, target):
        """
        :type target: int
        :rtype: int
        """
        target = abs(target)
        s = 0
        i = 1
        times = 0
        while True:
            s += i
            i += 1
            times += 1
            if s == target:
                return times
            if s > target:
                diff = s - target
                if diff % 2:
                    continue
                else:
                    return times


