class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hm = {}

        for i,n in enumerate(nums):
            diff = target-n
            if diff in hm:
                if hm[diff]<i:
                    return [hm[diff],i]
                else:
                    return [i,hm[diff]]
            hm[n] = i
        
        