class Solution:
    def maxArea(self, heights: List[int]) -> int:
        left = 0

        right = len(heights)-1
        max_area = max(heights[left],heights[right]) * (right-left)


        while left<right:
            if heights[left+1] > heights[left]:

                left+=1

                max_area = max(max_area,max(heights[left],heights[right]) * (right-left))
            elif heights[right+1] > heights[right]:
                right -=1
                max_area = max(max_area,max(heights[left],heights[right]) * (right-left))
            else:
                left+=1

        return max_area