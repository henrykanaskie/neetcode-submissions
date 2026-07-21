class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        preMap = {i: [] for i in range(numCourses)}
        for course, pre in prerequisites:
            preMap[course].append(pre)

        path = set()
        def dfs(crs, path):
            if crs in path:
                return False
            if preMap[crs] == []:
                return True
            path.add(crs)
            for pres in preMap[crs]:
                if not dfs(pres, path):
                    return False
            path.remove(crs)
            preMap[crs] = []
            return True
            
        
        for crs, _ in prerequisites:
            if dfs(crs, path) == False:
                return False

        return True