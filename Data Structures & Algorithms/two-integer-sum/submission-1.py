class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # nums.sort()
        # print(nums)
        for i in range(len(nums)):
            new_target = target - nums[i]
            for j in range(i+1, len(nums)):
                if new_target == nums[j]:
                    return [i, j]
        