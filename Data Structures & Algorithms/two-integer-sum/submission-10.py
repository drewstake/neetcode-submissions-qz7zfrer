class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashset = {}

        for i, num in enumerate(nums):
            wanted = target - num

            
            if wanted in hashset:
                return [hashset[wanted],i]
            hashset[num] = i

        