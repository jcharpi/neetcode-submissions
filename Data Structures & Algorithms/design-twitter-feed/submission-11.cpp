class Twitter {
public:
    void postTweet(int user_id, int tweet_id) {
        tweet_map[user_id].push_back({ curr_time, tweet_id });
        curr_time++;
    }

    vector<int> getNewsFeed(int user_id) {
        vector<int> valid_feed_user_ids{ user_id };
        if (follower_map.contains(user_id)) {
            const unordered_set<int>& followee_ids = follower_map[user_id];
            valid_feed_user_ids.insert(valid_feed_user_ids.end(), 
                followee_ids.begin(), followee_ids.end());
        }

        vector<CandidateTweet> candidate_tweets;
        candidate_tweets.reserve(valid_feed_user_ids.size());
        for (const int valid_feed_user_id : valid_feed_user_ids) {
            if (!tweet_map.contains(valid_feed_user_id)) {
                continue;
            }
            const vector<Tweet>& user_tweets = tweet_map[valid_feed_user_id];
            const ptrdiff_t newest_tweet_index = ssize(user_tweets) - 1;
            const Tweet& newest_tweet = user_tweets[newest_tweet_index];
            candidate_tweets.push_back({
                newest_tweet.timestamp,
                newest_tweet.tweet_id,
                valid_feed_user_id,
                newest_tweet_index,
            });
        }
        priority_queue<CandidateTweet> candidate_heap(candidate_tweets.begin(), candidate_tweets.end());

        vector<int> feed;
        feed.reserve(FEED_SIZE);
        while (!candidate_heap.empty() && ssize(feed) < FEED_SIZE) {
            const CandidateTweet newest = candidate_heap.top();
            candidate_heap.pop();
            feed.push_back(newest.tweet_id);

            if (newest.index > 0) {
                const ptrdiff_t older_index = newest.index - 1;
                const Tweet& older_tweet = tweet_map[newest.owner_id][older_index];
                candidate_heap.push({
                    older_tweet.timestamp,
                    older_tweet.tweet_id,
                    newest.owner_id,
                    older_index,
                });
            }
        }
        return feed;
    }

    void follow(int follower_id, int followee_id) {
        if (follower_id != followee_id) {
            follower_map[follower_id].insert(followee_id);
        }
    }

    void unfollow(int follower_id, int followee_id) {
        if (follower_map.contains(follower_id)) {
            follower_map[follower_id].erase(followee_id);
        }
    }

private:
    static constexpr ptrdiff_t FEED_SIZE = 10;

    struct Tweet {
        int timestamp;
        int tweet_id;
    };

    // A heap entry doubles as a cursor: it carries whose tweet this is and where
    // it sits in that user's list, so a pop can pull their next-newest tweet.
    struct CandidateTweet {
        int timestamp;
        int tweet_id;
        int owner_id;
        ptrdiff_t index;

        bool operator<(const CandidateTweet& other_candidate) const {
            return timestamp < other_candidate.timestamp;
        }
    };

    unordered_map<int, unordered_set<int>> follower_map; // user_id : [followee_ids]
    unordered_map<int, vector<Tweet>> tweet_map;         // user_id : [tweets, oldest first]
    int curr_time = 1;
};