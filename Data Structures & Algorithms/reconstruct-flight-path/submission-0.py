class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        adj = defaultdict(list)
        res = []
        for fromi, toi in sorted(tickets)[::-1]:
            adj[fromi].append(toi)
        
        stack = ["JFK"]
        while stack:
            curr = stack[-1]
            if not adj[curr]:
                res.append(stack.pop())
            else:
                stack.append(adj[curr].pop())
            
        return res[::-1]