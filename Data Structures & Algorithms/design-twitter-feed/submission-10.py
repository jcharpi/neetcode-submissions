class Twitter:
    def __init__(self):
        self.user_map = defaultdict(set)  # user_id : [followee_ids]
        self.tweets = defaultdict(list)  # user_id : [(count, tweet_id)]
        self.time = 1

    def postTweet(self, user_id: int, tweet_id: int) -> None:
        self.tweets[user_id].append((self.time, tweet_id))
        self.time += 1

    def getNewsFeed(self, user_id: int) -> List[int]:
        valid_feed_user_ids = [user_id]
        valid_feed_user_ids.extend(self.user_map.get(user_id, set()))

        # newest tweets from each user
        candidate_tweets = []
        for valid_feed_user_id in valid_feed_user_ids:
            user_tweets = self.tweets.get(valid_feed_user_id)
            if not user_tweets:
                continue

            newest_tweet_index = len(user_tweets) - 1
            timestamp, tweet_id = user_tweets[newest_tweet_index]
            candidate_tweets.append((
                timestamp,
                tweet_id,
                valid_feed_user_id,
                newest_tweet_index,
            ))

        heapq.heapify_max(candidate_tweets)

        news_feed = []
        while candidate_tweets and len(news_feed) < 10:
            timestamp, tweet_id, valid_feed_user_id, index = heapq.heappop_max(
                candidate_tweets
            )
            news_feed.append(tweet_id)

            if index > 0:
                older_timestamp, older_tweet_id = self.tweets[valid_feed_user_id][index - 1]
                heapq.heappush_max(
                    candidate_tweets,
                    (older_timestamp, older_tweet_id, valid_feed_user_id, index - 1),
                )

        return news_feed

    def follow(self, follower_id: int, followee_id: int) -> None:
        if follower_id != followee_id:
            self.user_map[follower_id].add(followee_id)

    def unfollow(self, follower_id: int, followee_id: int) -> None:
        self.user_map[follower_id].discard(followee_id)