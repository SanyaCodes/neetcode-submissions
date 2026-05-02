class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        t = len(temperatures)
        res = [0]*t
        stack = [] # stores indexes

        for i in range(t):
            
            # do something
            while stack and temperatures[i]>temperatures[stack[-1]]:
                last = stack.pop()
                res[last] = i-last
            
            stack.append(i)

        return res
