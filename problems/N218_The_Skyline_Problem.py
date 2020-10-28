import heapq

class Maxpq:
    def __init__(self):
        self.pq = []

    def front(self):
        return 0 if not self.pq else -self.pq[0]

    def push(self, h):
        heapq.heappush(self.pq, -h)

    def remove(self, h):
        self.pq.remove(-h)
        heapq.heapify(self.pq)

"""
Split the buildings into two different events : start and end event. 
Use a priority queue to maintain all valid height. 
If there is a start event, and if it's height > current max height in the priority queue, then add it into res. 
if it's height <= current max height, don't add it into res. 
    add the new heigth into the priority queue. 
    Because, maybe later we have end event, the higher height might be popped out before those smaller height. 
    
If there is an end event, we first remove it from the priority queue. Then check if the remove change the max height of the priority queue.
If the max height < the height of the end event, we need to add x and max height of the priority queue. 

Here are some key points:
    How to sort events.
    1. First sort event according to x (increasing)
    2. If x is equal, then we sort event according to it's type (start event should first than end event)
        if x is equal and end before end, then we will add (x, 0) invalid res.
    3. Then if start event, we sort it as decreasing, if end event, we sort it as increasing
        a. For start , we want to meet larger height first, so add it , won't change the pq's max height later.
        b. For end, we want to meet smaller height first, so remove it, won't change pq's max height.
    
    events.sort(key=lambda x: (x[0], x[2], x[2]*x[1]))
    
For python, heapq is minimum queue, so we use - height to turn it inot maximum queue. 
heapq doesn's support remove. so we need to write a wrapper . remove on the list, then heapq.heapify. But this causes TLE!!!
"""
class Solution(object):
    def getSkyline_TLE(self, buildings):
        """
        :type buildings: List[List[int]]
        :rtype: List[List[int]]
        """
        events = []
        for l, r, h in buildings:
            events.append((l, h, -1))
            events.append((r, h, 1))
        events.sort(key=lambda x: (x[0], x[2], x[2]*x[1]))

        res, pq = [], Maxpq()
        for x, h, t in events:
            if t == -1:
                if h > pq.front():
                    res.append([x, h])
                pq.push(h)
            else:
                pq.remove(h)
                if h > pq.front():
                    res.append([x, pq.front()])
        return res

    """
    for x, negH, R in event:
        1. make sure current highest building is still vaild --> pop highest building if it's R < x
        2. If event is a start of a building, push it into hp
        3. If #1 or #2 changes the current highest building, update the res. res[-1] contains the last height. If the current height is 
            not same as it , then update the res(maybe higher, maybe shorter).
    """
    def getSkyline_(self, buildings):
        # sort by
        # 1. x - we sweep line from left to right
        # 2. event type - we add building before remove ， also descreasing by height.
        events = sorted([(L, -H, R) for L, R, H in buildings] + list({(R, 0, None) for _, R, _ in buildings}))
        res, hp = [[0, 0]], [(0, float("inf"))]
        for x, negH, R in events:
            while x >= hp[0][1]:
                heapq.heappop(hp)
            if negH:
                heapq.heappush(hp, (negH, R))
            if res[-1][1] + hp[0][0]:
                res += [x, -hp[0][0]],
        return res[1:]
