import bisect
import collections
from typing import List


class TweetCounts:

    def __init__(self):
        self.user = collections.defaultdict(list)

    def recordTweet(self, tweetName: str, time: int) -> None:
        bisect.insort_left(self.user[tweetName], time)

    def getTweetCountsPerFrequency(self, freq: str, tweetName: str, startTime: int, endTime: int) -> List[int]:
        if freq == 'minute':
            length = 60
        elif freq == 'hour':
            length = 60 * 60
        else:
            length = 60 * 60 * 24
        ans = [0] * ((endTime - startTime) // length + 1)
        for t in self.user[tweetName]:
            if t < startTime:
                continue
            if t > endTime:
                break
            ans[(t - startTime) // length] += 1
        return ans


# Your TweetCounts object will be instantiated and called as such:
# obj = TweetCounts()
# obj.recordTweet(tweetName,time)
# param_2 = obj.getTweetCountsPerFrequency(freq,tweetName,startTime,endTime)