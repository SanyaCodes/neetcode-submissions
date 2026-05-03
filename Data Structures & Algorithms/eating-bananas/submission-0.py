class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        import math

        mp = max(piles)
        if len(piles) == h:
            return mp
        
        l,r,min_rate = 1,mp,mp

        while l<=r:
            mid = (l+r)//2
            
            hours = 0
            for p in piles:
                hours+=math.ceil(p/mid)

            # search left arr
            if hours<=h:
                min_rate = mid
                r = mid-1
            
            # search right arr
            else:
                l = mid+1

        return min_rate   

            
        