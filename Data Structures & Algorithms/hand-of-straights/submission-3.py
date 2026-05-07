class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False
        target = len(hand) // groupSize 
        hand.sort()
        count = Counter(hand)
        def getMin():
            new_min = -1
            min_pointer = 0
            while new_min == -1 or min_pointer < len(hand):
                arr_min = hand[min_pointer]
                if count[arr_min] > 0:
                    new_min = arr_min
                    break
                min_pointer += 1
            return new_min
        group = 0
        while group < target:
            start = getMin()
            if start != -1:
                pointer = 0
                while pointer < groupSize:
                    if count[start]>0:
                        count[start] -= 1
                        start += 1
                        pointer += 1
                    else:
                        return False
                group += 1
            else:
                return False
        return True
        
        