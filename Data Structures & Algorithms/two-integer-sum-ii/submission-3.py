class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        # numset = set(numbers)
        # ans = []
        # mp = {i+1: num for i, num in enumerate(numbers)}
        # for i in range(1, len(numbers)+1):
        #     val = target-mp[i]
        #     if val in numset:
        #         for key in mp:
        #             if mp[key] == val:
        #                 ans.append(min(i, key))
        #                 ans.append(max(i, key))
        #                 return ans

        f, l = 0, len(numbers)-1

        while f < l:
            val = numbers[f] + numbers[l]
            if val > target:
                l -= 1
            elif val < target:
                f += 1
            else:
                return [f+1, l+1]
        


