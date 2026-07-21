class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        adj = defaultdict(list)
        for s, d, c in flights:
            adj[s].append((d, c))
        prices = [float('inf')] * n
        prices[src] = 0
        for i in range(k+1):
            new_prices = prices.copy()
            for s, d, p in flights:
                if prices[s] == float("inf"):
                    continue
                if prices[s] + p < new_prices[d]:
                    new_prices[d] = prices[s] + p

            prices = new_prices
        return -1 if prices[dst] == float('inf') else prices[dst]