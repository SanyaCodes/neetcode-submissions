class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals)==1:
            return intervals

        intervals.sort(key = lambda x: x[0])
        # print(intervals)

        res = []

        l = intervals[0][0]
        r = intervals[0][1]
        
        for i in range(1, len(intervals)):
            if l<=intervals[i][0]<=r:
                if r<intervals[i][1]:
                    r = intervals[i][1]
            if intervals[i][0]>r:
                res.append([l,r])
                l = intervals[i][0]
                r = intervals[i][1]
        res.append([l,r])
        return res




            
        