class Solution(object):
    def candy_twopass(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        if not ratings:
            return 0
        length = len(ratings)
        res = [1]*length
        for i in range(1,length):
            if ratings[i] > ratings[i-1]:
                res[i] = res[i-1] + 1

        for i in range(length-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                res[i] = max(res[i], res[i+1]+1)

        return sum(res)

    """
    Calculate peak and bottom. 
    1. all bottoms should only have 1 candy
    2. as we move to peak, the left and right part will increase by one
    3. the peak itself will be the max(mostleft, mostright)
    4. we need to minus 1, because each time, we add left bottom which is last time's right bottom. so we need to set sum=1 at first time
    5. also don't forget to deal with there are many bottoms together.
    """
    def candy(self, ratings):
        if not ratings:
            return 0
        length = len(ratings)
        i, s = 0, 0
        sum = 1
        while i < length - 1:
            while i < length - 1 and ratings[i+1] > ratings[i]:
                i += 1
            left = i - s
            s = i
            while i < length - 1 and ratings[i+1] < ratings[i]:
                i += 1
            right = i - s
            s = i
            maximum = max(left, right) + 1
            sum += (1+left)*left // 2 + (1+right)*right// 2 - 1 + maximum
            while i < length - 1 and ratings[i+1] == ratings[i]:
                sum += 1
                i += 1
            s = i
        return sum

