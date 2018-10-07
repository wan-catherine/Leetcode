class Solution:
    def largestRectangleArea_timeoutversion(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        return self.getMax(heights)

    def getMax(self, l):
        if len(l) == 0:
            return 0
        if len(l) == 1:
            return l[0]

        m = min(l)
        index = [-1]
        for i in range(len(l)):
            if l[i] == m:
                index.append(i)
        index.append(len(l))

        res = m * len(l)

        for j in range(1, len(index)):
            t = self.getMax(l[index[j - 1] + 1:index[j]])
            res = t if t > res else res

        return res

    def largestRectangleArea_stilltimeout(self, heights):
        positions = {}
        for i in range(len(heights)):
            if heights[i] in positions:
                positions[heights[i]].append(i)
            else:
                positions[heights[i]] = [i]
        res = 0
        for value,indexes in sorted(positions.items()):
            for i in indexes:
                tmp = self.getRec(value, i, heights)
                res = tmp if tmp > res else res
                heights[i] = 0
        return res

    def getRec(self,value, i, heights):
        for x in range(i-1,-1,-1):
            if heights[x] == 0:
                left = x
                break
        else:
            left = -1
        for x in range(i+1, len(heights)):
            if heights[x] == 0:
                right = x
                break
        else:
            right = len(heights)
        return value*(right - left - 1)

    def largestRectangleArea(self, heights):
        if len(heights) == 0:
            return 0
        # if len(heights) == 1:
        #     return heights[0]

        indexes = []
        i = 0
        res = 0
        length = len(heights)
        heights.append(-1)
        while True:
            if i < length and (len(indexes) == 0 or heights[i] >= heights[indexes[-1]]):
                indexes.append(i)
                i += 1
            else:
                while len(indexes) > 0 and heights[indexes[-1]] > heights[i]:
                    index = indexes.pop()
                    if len(indexes) > 0:
                        temp = (i - indexes[-1] - 1)*heights[index]
                    else:
                        temp = i*heights[index]
                    res = temp if temp > res else res
            if i < length and len(indexes) == 0:
                heights[i - 1] = heights[i]
                indexes.append(i - 1)
            if i == length and len(indexes) == 0:
                break
        return res
