"""
monotonic stack

we need to maintain a monotonic non-decreasing stack which length equals to the most number of chunks
for each chunk, we only keep the largest number in the stack.

Here is an example :
    3,4,7,8,9,5
for all increasing number , each one can be one chunk
but if we meet some number is smaller , then it means it needs to move to stack head direction .
here '5' should be between 4 and 7. so 7,8,9,5 should be one chunk.

us monotonic stack

3,4,7,8,9   meet 5 whcih less than 9
3,4,        pop all numbers > 5
3,4,9       push the largest number of the chunk back to the stack

"""
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        stack = []
        max_num = 0
        for i in arr:
            if i > max_num:
                stack.append(i)
                max_num = i
            else:
                while stack and stack[-1] > i:
                    previous = stack.pop()
                    max_num = max(max_num, previous)
                stack.append(max_num)
        return len(stack)