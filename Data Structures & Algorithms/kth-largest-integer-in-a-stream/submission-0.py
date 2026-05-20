class KthLargest:

    import heapq

    def __init__(self, k: int, nums: List[int]):
        self.rank = k
        self.heap = nums
        heapq.heapify(self.heap)
        while len(self.heap)>k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        if len(self.heap)>self.rank:
            heapq.heappop(self.heap)
        return self.heap[0]
        

        
