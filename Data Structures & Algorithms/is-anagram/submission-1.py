class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s != s[::-1]:
            return False
        return True