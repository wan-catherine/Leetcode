from math import inf


class Solution(object):
    def findBestValue(self, arr, target):
        """
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        length = len(arr)
        arr.sort()
        prefix_sum = arr[:]
        for i in range(1, length):
            prefix_sum[i] += prefix_sum[i-1]

        mean_value = round(target/length)
        if arr[0] >= mean_value:
            return mean_value
        if arr[-1] <= mean_value:
            return arr[-1]

        left, right = arr[0], arr[-1] + 1
        while left < right:
            mid_value = (right - left) // 2 + left
            sum = self.get_sum(mid_value, arr, length)
            if sum > target:
                right = mid_value
            elif sum < target:
                left = mid_value + 1
            else:
                return mid_value
        sum_for_left = self.get_sum(left, arr, length)

        abs_left = abs(target - sum_for_left)
        abs_mid = abs(target - sum)
        if abs_left == abs_mid:
            return mid_value if mid_value < left else left
        elif abs_left > abs_mid:
            return mid_value
        else:
            return left

    def get_sum(self, mid_value, arr, length):
        sum = 0
        index = -1
        for i in range(length):
            if arr[i] < mid_value:
                sum += arr[i]
            else:
                index = i
                break
        if index != -1:
            sum += mid_value * (length - i)
        return sum

