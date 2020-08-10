import collections
from collections import deque


class Twitter(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user_tweet_mapping = collections.defaultdict(list)
        self.user_followee_mapping = collections.defaultdict(set)
        self.num = 0

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.num += 1
        self.user_tweet_mapping[userId].append((tweetId, self.num))

    def getNewsFeed(self, userId):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        :type userId: int
        :rtype: List[int]
        """
        tweets = self.user_tweet_mapping[userId][-10:]
        for id in self.user_followee_mapping[userId]:
            tweets.extend(self.user_tweet_mapping[id][-10:])
        tweets.sort(key=lambda x: x[1], reverse=True)
        return [tweet for tweet, num in tweets[:10]]

    def follow(self, followerId, followeeId):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId == followeeId:
            return
        self.user_followee_mapping[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.user_followee_mapping:
            return
        if followeeId not in self.user_followee_mapping[followerId]:
            return
        self.user_followee_mapping[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
obj = Twitter()
# obj.postTweet(1,5)
# print(obj.getNewsFeed(1))
# obj.follow(1,2)
# obj.postTweet(2,6)
# print(obj.getNewsFeed(1))
# obj.unfollow(1,2)
# print(obj.getNewsFeed(1))

obj.postTweet(1,5)
obj.postTweet(1,3)
obj.postTweet(1,101)
obj.postTweet(1,13)
obj.postTweet(1,10)
obj.postTweet(1,2)
obj.postTweet(1,94)
obj.postTweet(1,505)
obj.postTweet(1,333)
obj.postTweet(1,22)
obj.postTweet(1,11)


obj.follow(1,1)
print(obj.getNewsFeed(1))