class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()

        while n != 1:
            if n in seen:
                return False

            total = 0
            for x in str(n):
                total += int(x) ** 2

            seen.add(n)
            n = total

        return True


# Time complexity is O(k), where k is the number of iterations (small)
# Space complexity is O(k), where k is the size of the seen set