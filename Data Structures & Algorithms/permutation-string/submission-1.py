class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        k = len(s1)
        if len(s1) > len(s2):
            return False

        

        need = [0] * 26
        s2_cnt = [0] * 26

        for i in range(len(s1)):
            need[ord(s1[i]) - ord('a')] += 1
        

        for i, c in enumerate(s2):
            s2_cnt[ord(c) - ord('a')] += 1

                        
            if i >= k:
                s2_cnt[ord(s2[i - k]) - 97] -= 1

            if s2_cnt == need:
                return True

        

        return False
        
