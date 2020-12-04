import collections


class Solution(object):
    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        if not tasks:
            return 0

        nums = [0] * 26
        for task in tasks:
            nums[ord(task) - ord('A')] += 1
        nums.sort(reverse=True)
        ans = [[0] for _ in range(nums[0])]
        row = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[0]:
                use_last = True
            else:
                use_last = False
            while nums[i]:
                if nums[i] == 0:
                    continue
                ans[row].append(i)
                row += 1
                if use_last:
                    row = row % nums[0]
                else:
                    row = row %(nums[0]-1)
                nums[i] -= 1
        idle = 0
        for row in ans[:nums[0]-1]:
            while len(row) < n+1:
                row.append(None)
                idle += 1
        # print(ans)
        return len(tasks) + idle

    """
    An example:
        5A 5B 4C 4D 3E 2F 2G 1P  n = 4
        123456
        ABCDEP
        ABCDF
        ABCDF
        ABCEG
        ABDEG
        
    Consider from the most frequently tasks A. Then fill with the less frequently tasks BCD...
    If len(B) == len(A), easy, fill all frames (one A one frame)
    if len(C) < len(A), also easy, fill as much as possible, then fill by next less frequently task DEF...
    We don't need to worry about the D at the x-frame will at position d_x, and D will show at x-1_frame at 
    position d+1_x. This won't possbile. becasue len(D) < len(A).
    So for task D it always has distance >= n
    
    If all frames are filled, then for left taks , we can always find a correct position without using idle spot.
    because n is the least distance . 
    like ABCDEP , we can simply add it to one of the frame . 
    
    Here we also need to consider len(B/C/D..) == len(A) and len(B/C/D..) != len(A)
    if it's "!=", then we don't need to consider the last frame.
    if it's "==", we need to fill it into the last frame.
    """
    def leastInterval_other(self, tasks, n):
        if not tasks:
            return 0

        nums = [0] * 26
        for task in tasks:
            nums[ord(task) - ord('A')] += 1

        nums.sort()
        max_val = nums[25] - 1
        idle_slots = max_val * n
        for i in range(25):
            idle_slots -= min(nums[i], max_val)

        return idle_slots + len(tasks) if idle_slots >0  else len(tasks)

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        count = collections.Counter(tasks)
        length = len(tasks)
        arr = count.most_common()
        total = (arr[0][1] - 1) * (n + 1)

        left = 0
        for t, c in arr:
            if c >= arr[0][1]:
                left += c - arr[0][1] + 1
            else:
                break
        return max(length, total + left)
