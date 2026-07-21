class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = [] #(pair)
        res = [0] * len(temperatures)
        
        for i, temp in enumerate(temperatures):
            
        
            diff = 0
            while stack and temp > stack[-1][0]:
                t, index = stack.pop()
                diff = i - index
                res[index] = diff 
                    
            stack.append((temp, i))
        
        return res