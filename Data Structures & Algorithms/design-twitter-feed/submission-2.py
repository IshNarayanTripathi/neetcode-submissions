class Twitter:

    def __init__(self):
        self.timer = 0
        self.followers = defaultdict(set)
        self.feed = defaultdict(list)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.feed[userId].append((self.timer, tweetId))
        self.timer += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        people = self.followers[userId]|{userId}
        for person in people:
            tweet = self.feed[person]
            for ts, ti in tweet[-10:]:
                heapq.heappush(heap, (-ts, ti))
        result = []
        for _ in range(min(10, len(heap))):
            result.append(heapq.heappop(heap)[1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].discard(followeeId)
