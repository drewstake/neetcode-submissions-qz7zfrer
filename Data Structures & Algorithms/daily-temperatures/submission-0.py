class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)

        stack = [] # store (temp, index)

        for index, temp in enumerate(temperatures):
            while stack and stack[-1][0] < temp:
                t, idx = stack.pop()
                result[idx] = index - idx

            stack.append((temp,index))

        return result