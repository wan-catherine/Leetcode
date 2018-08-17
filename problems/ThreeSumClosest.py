class Solution:
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums = sorted(nums)
        minsum = float("inf")
        for i in range(len(nums) - 2):
            p = i + 1
            q = len(nums) - 1
            lesssum = float("inf") * (-1)
            moresum = float("inf")
            while p < q:
                sum = nums[i] + nums[p] + nums[q]
                if sum == target:
                    return target
                elif sum < target:
                    if sum > lesssum:
                        lesssum = sum
                    p += 1
                elif sum > target:
                    if sum < moresum:
                        moresum = sum
                    q -= 1
            if abs(minsum - target) > abs(lesssum - target) and abs(lesssum - target) < abs(moresum - target) :
                minsum = lesssum
            elif abs(minsum - target) > abs(moresum - target) and abs(moresum - target) < abs(lesssum - target):
                minsum = moresum
        return minsum





        