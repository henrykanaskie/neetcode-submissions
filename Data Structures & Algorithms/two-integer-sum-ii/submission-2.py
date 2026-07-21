class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        numset = set(numbers)
        ans = []
        mp = {i+1: num for i, num in enumerate(numbers)}
        for i in range(1, len(numbers)+1):
            val = target-mp[i]
            print(mp[i],val)
            if val in numset:
                print(val)
                for key in mp:
                    print(mp[key])
                    if mp[key] == val:
                        ans.append(min(i, key))
                        ans.append(max(i, key))
                        return ans
        


