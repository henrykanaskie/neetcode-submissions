class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        stack = []
        array = [[position[i], speed[i]] for i in range(len(position))]

        sortedArr = sorted(array, key=lambda x: x[0], reverse=True)

        for i in range(len(position)):
            
            time = (target - sortedArr[i][0]) / sortedArr[i][1]
            if stack and stack[-1] >= time:
                continue
            else:
                stack.append(time)

        
        return len(stack)



        