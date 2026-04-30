class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        max_area=float("-inf")
        rec=list()

        while l<r:
            curr_area = (r-l)*min(heights[l], heights[r])
            if curr_area>max_area:
                max_area = curr_area
                rec.append([heights[l], heights[r]])
            else:
                if heights[l]<heights[r]:
                    l += 1
                elif heights[r]<heights[l]:
                    r -= 1
                else:
                    l += 1
                    r -= 1
        print(rec)
        return max_area