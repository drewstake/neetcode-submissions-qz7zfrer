class Solution:
    def myPow(self, x: float, n: int) -> float:
        for _ in range(n-1):
            x = x * 2
            print(x)
        
        return x