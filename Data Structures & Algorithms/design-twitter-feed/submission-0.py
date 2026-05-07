class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.post = defaultdict(list)
        self.timestamp = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.timestamp += 1
        self.post[userId].append((self.timestamp, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        people = self.follows[userId]|{userId}
        for person in people:
            for ts, tid in self.post[person]:
                heapq.heappush(heap, (ts, tid))
                if len(heap) > 10:
                    heapq.heappop(heap)
        return [tid for _,tid in sorted(heap, reverse=True)]

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        
        self.follows[followerId].discard(followeeId)
