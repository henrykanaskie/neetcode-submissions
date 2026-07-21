class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
        path = []
        visited = set()
        def dfs(c, visited, path):
            if c in visited:
                return False
            if c in path:
                return True
                
            visited.add(c)
            for pre in preMap[c]:
                if not dfs(pre, visited, path):
                    return False
            path.append(c)
            visited.remove(c)
            return True
        
        for i in range(numCourses):
            if not dfs(i, visited, path):
                return []
        return path
        

        

