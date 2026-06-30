class Solution:
    def isValid(self, s: str) -> bool:
        closeToOpen = {')' : '(', '}' : '{', ']' : '['}
        stack = []

        for c in s:
            if c in closeToOpen and stack:
                if closeToOpen[c] != stack.pop():
                    return False

            
            else:
                stack.append(c)

        
        return True
