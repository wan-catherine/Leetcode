class Solution(object):
    def sampleStats(self, count):
        """
        :type count: List[int]
        :rtype: List[float]
        """
        res = [0]*5
        for i in range(256):
            if count[i] != 0:
                res[0] = i*1.0
                break
        for i in range(255,-1, -1):
            if count[i] != 0:
                res[1] = i*1.0
                break
        res[4] = count.index(max(count)) * 1.0
        val = 0
        num = 0
        for i in range(256):
            val += i * count[i]
            num += count[i]
        res[2] = val*1.0/num

        for i in range(1, 256):
            count[i] += count[i-1]

        n = count[-1] // 2
        if count[-1] % 2:
            for i in range(256):
                if count[i] < n:
                    continue
                res[3] = i * 1.0
                break
        else:
            for i in range(256):
                if count[i] < n:
                    continue
                if count[i] - n >= 2:
                    res[3] = i * 1.0
                else:
                    res[3] = (2*i + 1)*1.0/2
                break
        return res


