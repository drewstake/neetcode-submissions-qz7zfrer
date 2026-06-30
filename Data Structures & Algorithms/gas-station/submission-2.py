class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        pairs = [] # (gas, cost, i)
        res = 0
        MOD = len(gas)

        for i in range(len(gas)):
            ratio = gas[i] / cost[i]
            pairs.append((ratio, gas[i], cost[i], i))
    
        pairs.sort(reverse=True)
        print(pairs)

        tank = 0
        index = 0
        for _, gas, cost, i in pairs:
            tank += gas
            tank -= cost
            index += 1
            print(tank)
            if tank == 0 and index != len(pairs):
                return -1 
            
        return pairs[0][3]