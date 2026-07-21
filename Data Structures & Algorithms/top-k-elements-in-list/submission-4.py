class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mp = defaultdict(list)
        ans = list()
        if k == len(nums):
            return nums
        for num in nums:
            if num in mp:
                mp[num] += 1
            else:
                mp[num] = 1
        
        for i in range(k):
           
            maxval = max(mp.values())
            
            for key, val in mp.items():
                if val == maxval:
                    ans.append(key)
                    mp[key] = 0
                    break


        return ans