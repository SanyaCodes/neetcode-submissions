class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        from collections import deque
        que = deque()
        que.append(cost[-1])
        que.append(cost[-2])
        
        for i in range(n-3, -1, -1):
            if len(que)>2:
                que.popleft()
            if len(que)==2:
                que.append(min(que)+cost[i])
                print(que)
        que.popleft()
        return min(que)
            

            
        