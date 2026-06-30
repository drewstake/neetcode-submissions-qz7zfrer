class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits) - 1, -1, -1):
            if digits[i] == 9:
                j = i
                while digits[j] == 9:
                    digits[j] = 0
                    j-= 1
                    
                digits = [1] + digits
            else:
                digits[i] += 1
            break


        return digits