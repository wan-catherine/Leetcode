import collections
import heapq

"""
Use two dictionary:
one is num : count 
another one is : expected next number : count

We create 3 sequence first , then write the 4th number into the next_num_mapping 

"""
class Solution(object):
    def isPossible_(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        if not nums:
            return False

        num_count_mapping = collections.defaultdict(int)
        for num in nums:
            num_count_mapping[num] += 1

        next_num_mapping = collections.defaultdict(int)
        for num in nums:
            if num_count_mapping[num] == 0:
                continue
            if next_num_mapping[num] > 0:
                num_count_mapping[num] -= 1
                next_num_mapping[num] -= 1
                next_num_mapping[num+1] += 1
                continue
            for i in range(3):
                if num_count_mapping[num+i] == 0:
                    return False
                num_count_mapping[num+i] -= 1
            next_num_mapping[num+3] += 1

        return True

    # O(nlgn)
    def isPossible_hashtable(self, nums):
        tails = collections.defaultdict(list)
        for n in nums:
            count = 0
            if n - 1 in tails:
                count = heapq.heappop(tails[n - 1])
                if not tails[n - 1]:
                    del tails[n - 1]
            count += 1
            if n not in tails:
                tails[n] = []
                heapq.heappush(tails[n], count)
            else:
                heapq.heappush(tails[n], count)
        print(tails)
        for key, li in tails.items():
            if li[0] < 3:
                return False
        return True

    def isPossible(self, nums):
        counter = collections.Counter(nums)
        end = collections.defaultdict(int)

        for n in nums:
            if counter[n] == 0:
                continue
            if end[n-1] > 0:
                end[n-1] -= 1
                counter[n] -= 1
                end[n] += 1
            else:
                if counter[n+1] > 0 and counter[n+2] > 0:
                    counter[n+1] -= 1
                    counter[n] -= 1
                    counter[n+2] -= 1
                    end[n+2] += 1
                else:
                    return False
        return True