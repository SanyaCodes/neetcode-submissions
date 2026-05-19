class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        candidates.sort()
        result, subset = [], []
        n = len(candidates)

        def backtrack(i):

            if sum(subset) == target:
                result.append(subset.copy())
                return
            
            if sum(subset) > target or i == n:
                return
            
            subset.append(candidates[i])
            backtrack(i+1)
            subset.pop()
            
            while i+1 < n and candidates[i] == candidates[i+1]:
                i += 1
                
            backtrack(i+1)
            
        backtrack(0)
        return result

        