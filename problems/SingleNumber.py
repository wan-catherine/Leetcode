class Solution(object):
    def singleNumber_slow(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        check = []
        for i in nums:
            if i not in check:
                check.append(i)
            else:
                check.remove(i)
        return check[0]

    def singleNumber(self, nums):
        return 2*sum(set(nums)) - sum(nums) # 2∗(a+b+c)−(a+a+b+b+c)=c