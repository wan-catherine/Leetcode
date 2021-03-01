from collections import deque

"""
https://www.youtube.com/watch?v=D9Gy29pS4ec&feature=youtu.be

The key point, we need to save all information (time, speed) of the car before the current car when it collided . 

"""
class Solution(object):
    def getCollisionTimes(self, cars):
        """
        :type cars: List[List[int]]
        :rtype: List[float]
        """
        length = len(cars)
        res = [0] * length
        res[-1] = -1
        # here queue : from left to right, speed is decreasing.
        queue = deque()
        queue.append((0, cars[-1][1]))

        for i in range(length-2, -1, -1):
            diff = cars[i+1][0] - cars[i][0]
            cur_speed = cars[i][1]

            if cur_speed <= queue[-1][1]:
                queue.clear()
                queue.append((0, cur_speed))
                res[i] = -1
                continue

            time, speed = queue.popleft()
            total = 0
            while queue:
                if total + speed * (queue[0][0] - time) + diff >= cur_speed * queue[0][0]:
                    total += speed * (queue[0][0] - time)
                    time, speed = queue.popleft()
                else:
                    break

            dt = (diff - (cur_speed * time - total)) / (cur_speed - speed)
            queue.appendleft((dt + time, speed))
            queue.appendleft((0, cur_speed))
            res[i] = time + dt

        return res

