class Twitter:

    def __init__(self):
        self.user_map = defaultdict(set)
        self.tweets = defaultdict(list)
        self.time = 1

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        valid_tweets = list(self.tweets.get(userId, [])[-10:])
        for followeeId in self.user_map.get(userId, ()):
            valid_tweets.extend(self.tweets.get(followeeId, [])[-10:])

        return [tweetId for _, tweetId in heapq.nlargest(10, valid_tweets)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if (followerId != followeeId):
            self.user_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.user_map[followerId].discard(followeeId)
