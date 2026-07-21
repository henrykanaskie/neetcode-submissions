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
        
        list(mp.values())
        heap = []
        for val, freq in mp.items():
            heapq.heappush(heap, (-freq, val))

            
        for i in range(k):
            ans.append(heapq.heappop(heap)[1])

        return ans