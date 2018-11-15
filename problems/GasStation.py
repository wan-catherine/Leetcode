class Solution(object):
    def canCompleteCircuit_timeout(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        if sum(gas) < sum(cost):
            return  -1

        for i in range(len(gas)):
            if gas[i] < cost[i]:
                continue
            res = self.helper(i, gas, cost)
            if res != -1 :
                return res
        return -1

    def helper(self, index, gas, cost):
        i = 0
        left = 0
        while i <= len(gas):
            j = (index + i) % len(gas)
            left += gas[j]
            if left >= cost[j]:
                left -= cost[j]
                i += 1
            else:
                return -1
        return index

    def canCompleteCircuit(self, gas, cost):
        if sum(gas) < sum(cost):
            return  -1
        s = 0
        index = 0
        for i in range(len(gas)):
            s += gas[i] - cost[i]
            if s < 0:
                index = i + 1
                s = 0
        if s >= 0:
            return index
        return -1

