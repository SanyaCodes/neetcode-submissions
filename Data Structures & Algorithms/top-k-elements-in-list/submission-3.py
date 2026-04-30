class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = dict()
        res = []

        for num in nums:
            if num in d:
                d[num] += 1
            else:
                d[num] = 1
        
        d = dict(sorted(d.items(), key = lambda x: x[1], reverse = True))
        # print(d)

        for key,value in d.items():
            res.append(key)
            if len(res)==k:
                return res
            

        

        