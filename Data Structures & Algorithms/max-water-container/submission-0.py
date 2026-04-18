class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # 2 pointer
        # water contained = w = (j-i) * min(heights[i], heights[j])

        left = 0
        right = len(heights)-1
        max_w = 0

        while left < right:
            curr_w = (right-left)*min(heights[left], heights[right])
            if curr_w > max_w:
                max_w = curr_w
            if heights[left] < heights[right]:
                left += 1
            else:
                right -= 1
        
        return max_w

        