class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        pairs = [] # (gas, cost, i)
        res = 0
        MOD = len(gas)

        for i in range(len(gas)):
            pairs.append((gas[i], cost[i], i))
    
        pairs.sort(reverse=True)
        print(pairs)

        tank = 0

        for gas, cost, i in pairs:
            tank += gas
            tank -= cost
            if tank == 0:
                return -1

        return pairs[0][2]