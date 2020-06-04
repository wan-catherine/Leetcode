"""
i, j ,k
use decreasing monotonic stack from right
when nums[current] > nums[stack[-1]], it means we find j
in the stack, those < current are all possible be k
so the last step is to check from [0, current) , find i which nums[i] < nums[k]

here is a key point, how to find i.
brute solution, you can loop [0, current) and compare with all pop index.
or
use a list to maintain the minimum number from 0 to i.

each time, when we need to pop index from stack, we can check this number with the minvalue
________________________________________

From above explanation, I can stop myself thinking how about the a decreasing monotonic stack from left?
this way, when nums[current] > nums[stack[-1]], it means we find j
in the stack, those < current are possible be i

But then we find it difficult to find the k .
we need to loop all from [j+1:] and compare it to j and i .
It might cause timeout issue.

_________________________________________

So for those fixing three numbers problems, we first need to consider is monotonic stack
then need to consider how to fix and from which side to create the stack.

"""
class Solution(object):
    def find132pattern_timeout(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False
        nums_len = len(nums)
        for i in range(nums_len):
            if i + 1 < nums_len and nums[i] == nums[i + 1]:
                continue
            stack = []
            for j in range(i, nums_len):
                if j + 1 < nums_len and nums[j] == nums[j + 1]:
                    continue
                while stack and stack[-1] > nums[j]:
                    for k in stack:
                        if nums[j] > k :
                            return True
                        else:
                            break
                    break
                else:
                    stack.append(nums[j])
        return False

    def find132pattern(self, nums):
        if not nums:
            return False

        nums_len = len(nums)
        min_values = [nums[0]] * nums_len
        for i in range(1, nums_len):
            min_values[i] = min(min_values[i-1], nums[i])

        stack = []
        for i in range(nums_len-1, -1, -1):
            while stack and nums[stack[-1]] < nums[i]:
                index = stack.pop()
                if i > 0 and nums[index] > min_values[i-1]:
                    return True
            stack.append(i)
        return False