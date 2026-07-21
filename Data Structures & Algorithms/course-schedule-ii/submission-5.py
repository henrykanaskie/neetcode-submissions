class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        preMap = {i:[] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)
        path = []
        visited, cycle = set(), set()
        def dfs(c, visited, path):
            if c in visited:
                return True
            if c in cycle:
                return False

            cycle.add(c)
            for pre in preMap[c]:
                if not dfs(pre, visited, path):
                    return False
            cycle.remove(c)
            path.append(c)
            visited.add(c)
            return True
        
        for i in range(numCourses):
            if not dfs(i, visited, path):
                return []
        return path
        

        

