class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        n = len(nums)
        res = []

        from collections import deque

        que = deque()

        for i in range(n):
            # do something
            if len(que)==k:
                res.append(max(que))
                que.popleft()

            que.append(nums[i])

        res.append(max(que))

        return res


        