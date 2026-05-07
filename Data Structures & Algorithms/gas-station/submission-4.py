class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        for i in range(len(gas)):
            curr = i
            nex = (i+1)%len(gas)
            curr_gas = gas[i]
            updated_gas = curr_gas-cost[i]
            while updated_gas >= 0:
                if nex == curr:
                    return curr
                updated_gas += gas[nex] - cost[nex]

                
                nex = (nex + 1) % len(gas)
        return -1