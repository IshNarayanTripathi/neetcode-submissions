class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        for i in range(len(gas)):
            tank = gas[i]-cost[i]
            if tank < 0:
                continue
            j = (i+1)%len(gas)
            while j != i:
                tank += (gas[j]-cost[j])
                if tank < 0:
                    break
                j += 1
                j %= len(gas)
            if j == i:
                return i
        return -1
            