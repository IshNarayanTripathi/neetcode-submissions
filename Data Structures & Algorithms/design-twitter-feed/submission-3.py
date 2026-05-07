class Twitter:

    def __init__(self):
        self.follows = defaultdict(set)
        self.tweets = defaultdict(list)
        self.timer = 0

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.timer, tweetId))
        self.timer+=1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        people = self.follows[userId]|{userId}
        for person in people:
            for ts, ti in self.tweets[person][-10:]:
                heapq.heappush(heap, (-ts, ti))
        result = []
        for _ in range(min(10, len(heap))):
            result.append(heapq.heappop(heap)[1])
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follows[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follows[followerId].discard(followeeId)
