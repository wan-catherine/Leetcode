class Solution(object):
    def numOfSubarrays(self, arr, k, threshold):
        """
        :type arr: List[int]
        :type k: int
        :type threshold: int
        :rtype: int
        """
        length = len(arr)
        threshold *= k
        temp = sum(arr[:k])
        res = 0 if temp < threshold else 1
        for i in range(k, length):
            temp = temp + arr[i] - arr[i - k]
            if temp >= threshold:
                res += 1
        return res

