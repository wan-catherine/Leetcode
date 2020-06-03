"""
This problem I failed three time, the fourth time , finally success.
The most difficult part is considering duplicated number .

There are two parts where duplicated number will cause troubles :

First : the place we need to be replaced . test_maximumSwap_2
we need to find the minimum index

Second, the place we need to replace. test_maximumSwap_4
we need to find the maximum index

"""
class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        stack = []
        num_li = [int(x) for x in str(num)]
        num_len = len(num_li)
        index = num_len
        for i in range(num_len):
            while stack and num_li[stack[-1]] < num_li[i]:
                temp = stack.pop()
                index = min(index, temp)
            stack.append(i)
        if len(stack) == num_len:
            return num

        stack_index = index
        while stack_index + 1 < len(stack) and num_li[stack[stack_index + 1]] == num_li[stack[stack_index]]:
            stack_index += 1

        num_li[index], num_li[stack[stack_index]] = num_li[stack[stack_index]], num_li[index]
        return int("".join([str(i) for i in num_li]))



