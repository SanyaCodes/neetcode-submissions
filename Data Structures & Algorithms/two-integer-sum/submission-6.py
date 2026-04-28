class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        for i in range(len(nums)):
            res = []
            remainder = target - nums[i]
            res.append(i)
            for j in range(i+1,len(nums)):
                if nums[j] == remainder:
                    res.append(j)
                    return res
        
        