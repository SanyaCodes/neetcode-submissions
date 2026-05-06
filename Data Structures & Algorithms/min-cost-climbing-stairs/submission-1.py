class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        n = len(cost)

        if n==2:
            return min(cost)

        one = cost[-1]
        two = cost[-2]

        for i in range(n-3,-1,-1):
            temp = two
            two = cost[i] + min(one, two)
            one = temp
        
        return min(one,two)


        