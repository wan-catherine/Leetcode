class Solution:
    def grayCode_before(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]

        before = ["0","1"]
        after = []
        for i in range(2,n + 1):
            flag = True
            for index in range(len(before)):
                if flag == True:
                    after.append(before[index]+"0")
                    after.append(before[index]+"1")
                    flag = False
                else:
                    after.append(before[index] + "1")
                    after.append(before[index] + "0")
                    flag = True
            before = after
            after = []
        res = []
        for i in before:
            res.append(int(i, 2))
        return res

    def grayCode(self, n):
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        res = [0, 1]
        for i in range(2, n+1):
            arr = res[::-1]
            for j, v in enumerate(arr):
                arr[j] += 2**(i-1)
            res.extend(arr)
        return res