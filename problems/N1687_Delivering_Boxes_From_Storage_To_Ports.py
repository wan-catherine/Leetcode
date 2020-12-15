import sys
"""
dp[i] : ship all i boxes, the minimum number of trips needed. 
We need to consider two situation : 
1. greedy, we will carry as many boxes as possbile ( <=maxBoxes, <=maxWeight) 
    Here is problem:
    XXXXX i-1  i XXXXX j j+1 
    if j+1 has the same port as j, then it will be better put j , j+1 together. 
    
2. update last_j , so make sure all same ports boxes can be ship together. 
"""

class Solution(object):
    def boxDelivering(self, boxes, portsCount, maxBoxes, maxWeight):
        """
        :type boxes: List[List[int]]
        :type portsCount: int
        :type maxBoxes: int
        :type maxWeight: int
        :rtype: int
        """
        length = len(boxes)
        boxes = [[-1,0]] + boxes

        dp = [sys.maxsize] * (length+1)
        dp[0] = 0
        j, last_j, last_port = 0, 0, -1
        trips, weights = 0, 0

        for i in range(1, length+1):
            while j + 1 < length+1 and j+1-i+1 <= maxBoxes and weights + boxes[j+1][1] <= maxWeight:
                j += 1
                weights += boxes[j][1]
                if boxes[j][0] != boxes[j-1][0]:
                    trips += 1
                if boxes[j][0] != last_port:
                    last_j = j
                    last_port = boxes[j][0]
            dp[j] = min(dp[j], dp[i-1] + trips + 1)

            if j+1 < length + 1 and boxes[j+1][0] == boxes[j][0]:
                dp[last_j-1] = min(dp[last_j-1], dp[i-1] + trips + 1 - 1)

            weights -= boxes[i][1]
            trips -= (1 if i < length and boxes[i][0] != boxes[i+1][0] else 0)

        return dp[-1]
