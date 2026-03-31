class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest = 0
        numSet = set(nums)

        for num in nums:
            streak = 1
            curr = num + 1
            while curr in numSet:
                streak += 1
                curr += 1
            
            longest = max(streak, longest)

        
        return longest