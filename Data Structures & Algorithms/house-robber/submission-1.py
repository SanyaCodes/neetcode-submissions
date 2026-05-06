class Solution:
    def rob(self, nums: List[int]) -> int:
        
        x1,x2 = 0,0

        for n in nums:
            temp = x2
            x2 = max(x1+n,x2)
            x1 = temp
        
        return x2

        
        