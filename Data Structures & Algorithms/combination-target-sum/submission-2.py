class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        result, subset = [], []
        n = len(nums)

        def backtrack(i):

            # base case 1 - total matches target:
            if sum(subset) == target:
                result.append(subset.copy())
                return
            
            # base case 2 - end of nums reached or target crossed:
            if i == n or sum(subset) > target:
                return
            
            subset.append(nums[i])
            backtrack(i)
            subset.pop()
            backtrack(i+1)

        backtrack(0)
        return result

            

        
        