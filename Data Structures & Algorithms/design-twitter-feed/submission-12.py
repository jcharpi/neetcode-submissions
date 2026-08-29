class Twitter:
    FEED_SIZE = 10

    def __init__(self):
        self.follower_map = defaultdict(set)  # user_id : [followee_ids]
        self.tweet_map = defaultdict(list)    # user_id : [tweets, oldest first]
        self.curr_time = 1

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        self.tweet_map[user_id].append((self.curr_time, tweet_id))
        self.curr_time += 1

    def getNewsFeed(self, user_id: int) -> List[int]:
        valid_feed_user_ids = [user_id]
        valid_feed_user_ids.extend(self.follower_map.get(user_id, set()))

        candidate_tweets = []
        for valid_feed_user_id in valid_feed_user_ids:
            user_tweets = self.tweet_map.get(valid_feed_user_id)
            if not user_tweets:
                continue

            newest_tweet_index = len(user_tweets) - 1
            newest_timestamp, newest_tweet_id = user_tweets[newest_tweet_index]
            candidate_tweets.append((
                newest_timestamp,
                newest_tweet_id,
                valid_feed_user_id,
                newest_tweet_index,
            ))
        heapq.heapify_max(candidate_tweets)

        feed = []
        while candidate_tweets and len(feed) < self.FEED_SIZE:
            timestamp, tweet_id, owner_id, index = heapq.heappop_max(candidate_tweets)
            feed.append(tweet_id)

            if index > 0:
                older_index = index - 1
                older_timestamp, older_tweet_id = self.tweet_map[owner_id][older_index]
                heapq.heappush_max(
                    candidate_tweets,
                    (older_timestamp, older_tweet_id, owner_id, older_index),
                )

        return feed

    def follow(self, follower_id: int, followee_id: int) -> None:
        if follower_id != followee_id:
            self.follower_map[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.follower_map[follower_id].discard(followee_id)