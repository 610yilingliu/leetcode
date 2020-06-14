#
# @lc app=leetcode id=355 lang=python3
#
# [355] Design Twitter
#
import collections
import heapq
# @lc code=start
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.user_and_posts = collections.defaultdict(list)
        self.user_and_followers = collections.defaultdict(set)
        self.no = 0
        self.recent = 10

    def postTweet(self, userId, tweetId):
        """
        Compose a new tweet.
        """
        self.user_and_posts[userId].append([-self.no, tweetId])
        self.no += 1
        
    def getNewsFeed(self, userId: int):
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        heap = []
        for following in self.user_and_followers[userId]:
            for i in range(len(self.user_and_posts[following]) - 1, max(-1, len(self.user_and_posts[following]) - self.recent - 1), -1):
                heapq.heappush(heap, self.user_and_posts[following][i])
        for i in range(len(self.user_and_posts[userId]) - 1, max(-1, len(self.user_and_posts[userId]) - self.recent - 1), -1):
            heapq.heappush(heap, self.user_and_posts[userId][i])
        ans = []
        c = 0
        while heap and c < self.recent:
            ans.append(heapq.heappop(heap)[1])
            c += 1
        return ans

    def follow(self, followerId: int, followeeId: int):
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId != followeeId:
            self.user_and_followers[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int):
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if self.user_and_followers[followerId] and followeeId in self.user_and_followers[followerId]:
            self.user_and_followers[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(1,5)
# param_2 = obj.getNewsFeed(1)
# obj.follow(1,2)
# obj.postTweet(2,6)
# param_2 = obj.getNewsFeed(1)
# print(param_2)
# obj.unfollow(followerId,followeeId)
# @lc code=end

