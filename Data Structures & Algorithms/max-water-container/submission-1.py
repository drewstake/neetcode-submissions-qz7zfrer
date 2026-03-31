class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # starting on both sides, initialize pointers l and r
        l,r = 0,len(heights)-1
        maxSize = 0
        while l <r:
            left = heights[l]
            right = heights[r]
            distance = r-l

            currSize = distance* min(left,right)
            maxSize = max(currSize,maxSize)

            if left >right:
                r-=1
            else:
                l+=1
            
        return maxSize

