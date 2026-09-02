class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = {i: [] for i in range(numCourses)}
        visitset = set()
        for courses, prereq in prerequisites:
            pre[courses].append(prereq)
        def dfs(crs):
            if crs in visitset:
                return False
            if pre[crs] == []:
                return True
            visitset.add(crs)
            for prereq in pre[crs]:
                if not dfs(prereq):
                    return False
            visitset.remove(crs)
            pre[crs] = []
            return True
        for crs in range(numCourses):
            if not dfs(crs):
                return False
        return True
