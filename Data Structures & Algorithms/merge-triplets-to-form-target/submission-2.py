class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:

        ans = set()

        for a,b,c in triplets:
            if a>target[0] or b>target[1] or c>target[2]:
                continue
            if a==target[0]: ans.add(0)
            if b==target[1]: ans.add(1)
            if c==target[2]: ans.add(2)
        
        if len(ans)==3:
            return True
        return False

        