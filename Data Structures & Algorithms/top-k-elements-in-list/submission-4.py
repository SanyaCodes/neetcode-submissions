class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        from collections import defaultdict
        import heapq

        hm = defaultdict(int)

        for num in nums:
            hm[num] += 1

        result = [x for x,y in heapq.nlargest(k, hm.items(), key = lambda x: x[1])]

        print(hm.items())

        return result
        
        