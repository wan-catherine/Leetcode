class Solution(object):
    # two pointers : fast and slow pointers
    # similar to find cycle
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        p, q = nums[0], nums[0]
        while True:
            p = nums[p]
            q = nums[nums[q]]
            if p == q:
                break
        q = nums[0]
        while p != q:
            p = nums[p]
            q = nums[q]
        return p


    # first access, set it to negative , if it's a duplicated number,
    # then , when second access , if a number is a negative , it means
    # it's the second time to access, then we know it's the duplicate number
    # But this one also modify the array
    def findDuplicate_modify_array(self, nums):
        index = nums[0]
        while True:
            if nums[index] < 0:
                return index
            else:
                nums[index] = - nums[index]
            index = abs(nums[index])