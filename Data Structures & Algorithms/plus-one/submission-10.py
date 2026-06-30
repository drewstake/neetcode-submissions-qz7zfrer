class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        i = len(digits) - 1
        if digits[i] == 9:
            j = i
            while digits[j] == 9:
                digits[j] = 0
                j-= 1
            
            digits = [1] + digits
        else:
            digits[i] += 1


        return digits