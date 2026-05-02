class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        import heapq
        heap = [-n for n in nums]
        heapq.heapify(heap)

        count = 0

        while k>1:
            heapq.heappop(heap)
            k -= 1
        
        return -heapq.heappop(heap)
        