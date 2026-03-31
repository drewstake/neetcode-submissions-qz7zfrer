class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #generate all pairs
        import copy
        freq = {}
        pairs = []
        for num in nums:
            if num not in freq:
                freq[num] = 1
            else:
                freq[num] +=1
        
        for i in range(len(nums)-1):
            for j in range(i+1,len(nums)):
                pairs.append([nums[i],nums[j]])
        ans = set()
        for pair in pairs:
            deepcpy_freq = freq.copy()
            sumOfP1P2 = pair[0]+pair[1]
            deepcpy_freq[pair[0]] -=1
            deepcpy_freq[pair[1]] -=1

            if -sumOfP1P2 in deepcpy_freq and deepcpy_freq[-sumOfP1P2] >0:
                ans.add(tuple(sorted([pair[0],pair[1],-sumOfP1P2])))
        return [list(t) for t in ans]

