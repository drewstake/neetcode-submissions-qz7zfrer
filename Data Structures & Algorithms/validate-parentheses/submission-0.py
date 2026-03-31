class Solution:
    def isValid(self, s: str) -> bool:
        CloseToOpen = {')' : '(' , '}':'{', ']':'['}

        stack = []

        for c in s:
            if c not in CloseToOpen: # it's a opening
                stack.append(c)
            else:
                if len(stack) <= 0:
                    return False
                
                if stack[-1] != CloseToOpen[c]:
                    return False
                
                stack.pop()

        
        return len(stack) == 0
            
            
            