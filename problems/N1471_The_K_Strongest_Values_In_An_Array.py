class Solution(object):
    def getStrongest(self, arr, k):
        """
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        if not arr:
            return arr

        arr.sort()
        arr_len = len(arr)
        mid = (arr_len - 1) // 2
        res = []
        left,right = 0, arr_len-1
        while left < mid and right > mid and k > 0:
            if arr[right] - arr[mid] >= arr[mid] - arr[left]:
                res.append(arr[right])
                right -= 1
            else:
                res.append(arr[left])
                left += 1
            k -= 1
        if k == 0:
            return res
        while left < mid and k > 0:
            res.append(arr[left])
            left += 1
            k -= 1

        while right > mid and k > 0:
            res.append(arr[right])
            right -= 1
            k -= 1

        if k > 0:
            res.append(arr[mid])
        return res


