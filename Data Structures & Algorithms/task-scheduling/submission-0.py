class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        count = Counter(tasks)
        time = 0
        heap = [-c for c in count.values()]
        heapq.heapify(heap)

        q = deque()
        while heap or q:
            time += 1
            if not heap:
                time = q[0][1]
            else:
                c = 1 + heapq.heappop(heap)
                if c:
                    q.append([c, time + n])
            if q and q[0][1] == time:
                heapq.heappush(heap, q.popleft()[0])
            
        return time
                
            