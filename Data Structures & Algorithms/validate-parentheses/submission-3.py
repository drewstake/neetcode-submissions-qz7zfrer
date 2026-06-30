class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')' : '(', '}' : '{', ']' : '['}
        stack = []

        for c in s:
            if c in closeToOpen and not stack:
                if closetoOpen[c] != stack.pop():
                    return False

            
            else:
                stack.append(c)

        
        return True
