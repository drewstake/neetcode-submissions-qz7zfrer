class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1 = []
        s2 = []

        for c in s:
            s1.append(c)
        for c in t:
            s2.append(c)

        s1.sort()
        s2.sort()

        if s1 == s2:
            return True
        
        return False