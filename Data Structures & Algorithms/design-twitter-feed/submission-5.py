class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.post = defaultdict(list)
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timer += 1
        self.post[userId].append((tweetId, self.timer))

    def getNewsFeed(self, userId: int) -> List[int]:
        ids = self.follows[userId]|{userId}
        posts = []
        for id in ids:
            posts.extend(self.post[id])
        max_heap = [(-timer, tweet) for tweet, timer in posts]
        heapq.heapify(max_heap)
        res = []
        target = 10
        while target and max_heap:
            _, tweet = heapq.heappop(max_heap)
            res.append(tweet)
            target -= 1
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follows[followerId]:
            self.follows[followerId].remove(followeeId)
