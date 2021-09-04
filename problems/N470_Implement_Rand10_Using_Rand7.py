def rand7(self):
    pass
"""
Two points :
1. Rejection sampling. When you have a random list [1, x] , x >= 10, then you can use rejection sampling.
   Randomly get any number y from [1,x], if y >= 10, the reject and do it again. 
   This step we can give math approvement.
2. How to from 7 to get a [1,x] x >= 10 ? 
   First random7 + random7 will get a list [1, 14] , but it don't uniform random . 
   For example, 2 = 1 + 1, but 10 : 3+7, 4+6, 5+5... which has more possibility than 2. 
   
   we can use ab(base7) : 00 -> 66  (7 binary method), they are all have same possibility.
   0 ~ 48(7*7 index) , so when x >= 40  then reject. 
"""
class Solution(object):
    def rand10(self):
        """
        :rtype: int
        """
        index = 50
        while index >= 40:
            index = 7 * (rand7() - 1) + (rand7() - 1);
        return index % 10 + 1