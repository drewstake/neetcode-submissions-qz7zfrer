class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        point1 = 0
        point2 = len(numbers)-1
        num1 = numbers[point1]
        num2 = numbers[point2]
        s = num1 + num2

        while s != target:
            
            if s > target:
                point2 -= 1 
                num2 = numbers[point2]
            else:# s < target
                point1 += 1
                num1 = numbers[point1]
            s = num1 + num2
        #print(s)
        return [point1+1, point2+1]

              