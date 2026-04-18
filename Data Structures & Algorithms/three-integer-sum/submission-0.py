class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 2 pointer approach
        # since i dont need to return the indices, i can sort the nums array
        nums.sort()
        answer = []

        if len(nums) < 3:
            return False

        for i in range(len(nums)-2):
            # print(i)
            remainder = 0-nums[i]
            left = i+1
            right = len(nums)-1
            while left < right:
                if nums[left] + nums[right] < remainder:
                    left += 1
                elif nums[left] + nums[right] > remainder:
                    right -= 1
                else:
                    answer.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
        
        # print({tuple(t) for t in answer})
        
        return [list(t) for t in {tuple(t) for t in answer}]


        