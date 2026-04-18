class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        # the key here is to maintain a stack such that:
        # it only contains the indices that have not been solved for
        # temp[stack[0]] > temp[stack[1]]>...

        answer = [0]*len(temperatures)
        stack = []

        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                index = stack.pop()
                answer[index] = i-index
            stack.append(i)
        
        return answer
        