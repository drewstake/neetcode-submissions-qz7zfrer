class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # addition is taking the last two from the stack
        # multiplication is taking the last two from the stack
        # subtraction is taking the [i - 1] - [i]
        # division is taking the 

        stack = []

        for token in tokens:
            if token == "+":
                a = stack.pop()
                b = stack.pop()
                c = int(a) + int(b)
                stack.append(c)
                
            
            elif token == "-":
                x = stack.pop()
                y = stack.pop()
                z = int(y) - int(x)
                stack.append(z)
            

            elif token == "*":
                u = stack.pop()
                v = stack.pop()
                w = int(v) * int(u)
                stack.append(w)
            
            elif token == "/":
                p = stack.pop()
                q = stack.pop()
                r = int(q) / int(p)
                stack.append(r)
            
            else:
                stack.append(token)
            

            print(stack)
        
        return int(stack[0])