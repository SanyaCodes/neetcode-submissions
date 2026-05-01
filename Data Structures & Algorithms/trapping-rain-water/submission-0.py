class Solution:
    def trap(self, height: List[int]) -> int:
        # l and r at 0 and 1
        # if height of l > height of r move r until height of r > height of l
        # record seen areas, seen.append(seen H)
        # if reached, add area to res
        # area = min(h[l],h[r])*(r-l)-seen units
        
        l, r = 0, len(height)-1
        hl_max, hr_max = height[l], height[r]
        res = 0

        while l<r:
            if hl_max < hr_max:
                l+=1
                hl_max = max(hl_max, height[l])
                res += hl_max - height[l]
            else:
                r -= 1
                hr_max = max(hr_max, height[r])
                res += hr_max - height[r]
            
        return res 
        
