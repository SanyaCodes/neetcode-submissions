class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        curmax,ans = 0,max(nums)

        for n in nums:
            curmax = max(curmax+n,n)
            ans = max(ans,curmax)

        return ans