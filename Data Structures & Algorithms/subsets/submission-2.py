class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)
        result, subset = [], []

        def backtrack(i,subset):

            if i == n:
                return [subset]

            include = backtrack(i+1,subset+[nums[i]])
            exclude = backtrack(i+1,subset)

            return include + exclude
            
        return backtrack(0,subset)

