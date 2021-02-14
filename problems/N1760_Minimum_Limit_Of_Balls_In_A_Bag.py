class Solution:
    def minimumSize(self, nums, maxOperations: int) -> int:
        def check(val):
            nonlocal maxOperations
            oper = 0
            for num in nums:
                oper += (num - 1) // val
                if oper > maxOperations:
                    return False
            return True

        left, right = 1, 10 ** 9 + 1
        while left < right:
            mid = (right - left) // 2 + left
            if check(mid):
                right = mid
            else:
                left = mid + 1
        return left