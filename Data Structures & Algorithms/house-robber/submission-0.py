class Solution:
    def rob(self, nums: List[int]) -> int:

        x1, x2 = 0, 0

        for n in nums:
            temp = max(x1+n, x2)
            x1 = x2
            x2 = temp
        
        return x2
        