class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        curmax, curmin, ans = 1,1,max(nums)

        for n in nums:
            if n==0:
                curmax, curmin = 1,1
                continue
            temp = curmax*n
            curmax = max(curmax*n,curmin*n,n)
            curmin = min(temp,curmin*n,n)
            ans = max(curmax,ans)

        return ans

        