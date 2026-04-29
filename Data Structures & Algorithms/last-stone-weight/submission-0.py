class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        import heapq

        # heap is by default a min-heap
        # so we need to convert it to a max-heap here

        heap = [-s for s in stones]
        heapq.heapify(heap) # ---> O(n)

        while len(heap) > 1:
            y = -1 * heapq.heappop(heap)
            x = -1 * heapq.heappop(heap)

            if x < y:
                heapq.heappush(heap,-(y-x))

        return -heap[0] if heap else 0
            

            
            
        