import collections

"""
for a range, we need to get the most popular number , then use the total - popular which equals 
to the number we need to change . 
"""
class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        counter = collections.defaultdict(int)
        left, length, res = 0, len(answerKey), 0
        for i in range(length):
            counter[answerKey[i]] += 1
            while i - left + 1 - max(counter.values()) > k:
                counter[answerKey[left]] -= 1
                left += 1
            res = max(res, i - left + 1)
        return res