import random
"""
weight random algo

use an array to keep the prefix sum of the weight array.
then for any picIndex, we can randomly create a number which is between [1， sum(w)].
this way , we can randomly picks an index in proportion to it's weight. 

Here is an example : 
w = [1,3,6]
prefix_sum = [1,4,10]
for any number between 1~10 : 1,2,3,4,5,6,7,8,9,10
1: 1
3: 2,3,4
6: 5,6,7,8,9,10

use binary search (must notice the <= left and right, mid change!!!)
    if use : left < right : then right = mid 
    if use : left <= right, then right = mid - 1

"""

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """

        self.pre_sum = w
        self.len = len(w)
        for i in range(1,self.len):
            self.pre_sum[i] += self.pre_sum[i-1]

    def pickIndex(self):
        """
        :rtype: int
        """
        w_sum = self.pre_sum[-1]
        l = 0
        r = self.len - 1
        num = random.randint(1, w_sum)
        while l < r:
            mid = l + (r - l) // 2
            if self.pre_sum[mid] < num:
                l = mid + 1
            elif self.pre_sum[mid] > num:
                r = mid
            else:
                return mid
        return l

if __name__ == "__main__":
    w = [1,3,1]
    obj = Solution(w)
    obj.pickIndex()

