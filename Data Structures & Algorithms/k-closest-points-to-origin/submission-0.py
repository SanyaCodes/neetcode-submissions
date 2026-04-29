class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        import math
        from collections import defaultdict
        res = defaultdict(list)

        for point in points:
            x = point[0]
            y = point[1]
            dist = math.sqrt(x**2 + y**2)
            res[dist].append(point)
        
        res = dict(sorted(res.items()))

        ans = []

        for key,v in res.items():
            for i in v:
                ans.append(i)
                if len(ans) == k:
                    return ans
        

            





        