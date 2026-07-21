class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n-1):
            return False

        edgeMap = {i:[] for i in range(n)}
        for source, edge in edges:
            edgeMap[source].append(edge)
            edgeMap[edge].append(source)
        visited = set()
        
        def dfs(node, par):
            
            if node in visited:
                return False
            visited.add(node)    
            for edge in edgeMap[node]:
                if edge == par:
                    continue
                if not dfs(edge, node):
                    return False
            return True

        return dfs(0,-1) and len(visited) == n
        

        