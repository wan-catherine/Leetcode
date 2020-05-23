class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums or len(nums) < 4:
            return []
        nums_len = len(nums)
        nums = sorted(nums)
        res = []
        last_item = nums[-1]
        for i in range(nums_len-3):
            if i >0 and nums[i] == nums[i-1]:
                continue
            if nums[i] * 4 > target:
                break
            if nums[i] + 3 * last_item < target:
                continue
            for j in range(i+1, nums_len-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue
                if nums[i] + nums[j]*3 > target:
                    break
                if nums[i] + nums[j] + last_item*2 < target:
                    continue
                base = target - nums[i] - nums[j]
                p, q = j + 1, nums_len-1
                while p < q:
                    if p > j + 1 and nums[p] == nums[p - 1]:
                        p += 1
                        continue
                    if q < nums_len-1 and nums[q] == nums[q+1]:
                        q -= 1
                        continue

                    if nums[p] + nums[q] == base:
                        res.append([nums[i], nums[j], nums[p], nums[q]])
                        p += 1
                        q -= 1
                    elif nums[p] + nums[q] > base:
                        q -= 1
                    else:
                        p += 1

        return res

    # amazing!
    # do our best to reduce the travel times(see the break and continue condition)
    def fourSum_fast(self, nums, target):
        if len(nums) == 0:
            return []
        nums.sort()
        U, V, W, Z = len(nums), {j: i for i, j in enumerate(nums)}, set(), nums[-1]
        for i in range(0, U - 3):
            a = nums[i]
            if a * 4 > target:
                break
            if a + 3 * Z < target:
                continue
            for j in range(i + 1, U - 2):
                b = nums[j]
                if a + b * 3 > target:
                    break
                if a + b + 2 * Z < target:
                    continue
                for k in range(j + 1, U - 1):
                    c = nums[k]
                    if a + b + 2 * c > target:
                        break
                    if a + b + c + Z < target:
                        continue
                    d = target - a - b - c
                    if (d in V) and V[d] > k:
                        W.add((a, b, c, d))
        return W