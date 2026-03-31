class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        arr = list(map(int, str(n))) # [1, 0, 1]
        while True:
            total = 0
            for num in arr:
                total += num ** 2
            if total == 1:
                return True
            if total in seen:
                return False
            
            seen.add(total)
            arr = list(map(int, str(total))) 