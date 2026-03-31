class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = r = 0
        high = 0
        seen = set()

        while l < len(s) and r < len(s):
            if s[r] not in seen:
                seen.add(s[r])
                high = max(high, r - l + 1)
                r += 1
            else:
                seen.remove(s[l])
                l += 1

        return high
