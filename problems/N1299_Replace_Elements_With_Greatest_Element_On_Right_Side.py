class Solution(object):
    def replaceElements(self, arr):
        """
        :type arr: List[int]
        :rtype: List[int]
        """
        if not arr:
            return None
        arr_len = len(arr)
        max_num = arr[-1]
        arr[-1] = -1
        for i in range(arr_len-2, -1, -1):
            previous = arr[i]
            arr[i] = max_num
            max_num = max(max_num,previous )
        return arr

