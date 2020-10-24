class Solution(object):
    def addNegabinary_(self, arr1, arr2):
        """
        :type arr1: List[int]
        :type arr2: List[int]
        :rtype: List[int]
        """
        def get_num(arr):
            num = 0
            for i, v in enumerate(arr):
                num *= (-2)
                num += v
            return num

        num = get_num(arr1) + get_num(arr2)

        res = []
        while num:
            res.append(num & 1)
            num = -(num // 2)
        return res[::-1] or [0]

    def addbinary(self, arr1, arr2):
        res = []
        carry = 0
        while arr1 or arr2 or carry:
            carry += (arr1 or [0]).pop() + (arr2 or [0]).pop()
            res.append(carry & 1)
            carry = carry >> 1
        return res[::-1]

    def addNegabinary(self, arr1, arr2):
        res = []
        carry = 0
        while arr1 or arr2 or carry:
            carry += (arr1 or [0]).pop() + (arr2 or [0]).pop()
            res.append(carry & 1)
            carry = -(carry >> 1)
        while len(res) > 1 and res[-1] == 0:
            res.pop()
        return res[::-1]