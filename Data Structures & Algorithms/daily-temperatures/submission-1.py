class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] # [(30, 0)]
        res = [0] * len(temperatures) #

        for index, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                tmp, i = stack.pop()
                res[i] = index - i
            stack.append((temp, index))
            print(stack)
        
        return res