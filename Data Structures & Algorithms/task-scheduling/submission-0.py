class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        rep = [0]*26
        
        for task in tasks:
            rep[ord(task)-ord('A')] += 1
        
        max_freq = max(rep)
        count_freq = rep.count(max_freq)

        arr = (max_freq-1)*(n+1) + count_freq       

        return max(arr, len(tasks)) 