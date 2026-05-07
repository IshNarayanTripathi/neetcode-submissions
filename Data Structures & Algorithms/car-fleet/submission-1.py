class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        new = list(zip(position, speed))
        new.sort(key=lambda x: x[0], reverse=True)
        stack = []
        i = 0
        while i < len(position):
            curr_time = (target-new[i][0])/new[i][1]
            if stack and stack[-1]>=curr_time:
                i+=1
                continue
            stack.append(curr_time)
            i+=1
        return len(stack)