class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        newlist = sorted(zip(position, speed), key = lambda x: x[0], reverse = True)
        stack = []
        for p,s in newlist:
            time = (target-p)/s
            if stack and stack[-1] >= time:
                continue
            stack.append(time)
        return len(stack)
