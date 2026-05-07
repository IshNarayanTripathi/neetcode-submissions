class Twitter:

    def __init__(self):
        self.timer = 0
        self.followers = defaultdict(set)
        self.feed = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed[userId].append((self.timer, tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = self.feed[userId][:]
        for follower in self.followers[userId]:
            feed.extend(self.feed[follower])
        feed.sort(key=lambda x: -x[0])
        return [tweetId for _,tweetId in feed[:10]]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
