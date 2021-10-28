class Solution:
    def singleNumber_before(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        nums = sorted(nums)
        l = len(nums)
        i = 0
        j = 1
        res = []
        while j < l:
            if nums[i] == nums[j]:
                i += 2
                j += 2
            else:
                res.append(nums[i])
                i += 1
                j += 1
        if len(res) < 2:
            res.append(nums[i])
        return res

    """
    This is a super pretty bit manipulation problem.
    
    0 ^ x = x
    x ^ x = 0
    
    1. xor for all num in nums, the we will get a^b = base.
    2. find the right most set bit : base &= ~(base - 1) 
    3, loop the whole nums, base&num
    
    when we find the right most set bit number: x , then a & x > 0 , b & x == 0
    for all other numbers , we have two each of them : n , no matter n & x > or = 0 , it will become 0 for : a/b ^ num ^ num . 
    """
    def singleNumber(self, nums):
        res = [0,0]
        base = 0
        for num in nums:
            base ^= num
        base &= ~(base - 1)  # lowbit(base) = base & (-base)

        for num in nums:
            if num & base > 0:
                print(num)
                res[0] ^= num
            else:
                res[1] ^= num
        return res