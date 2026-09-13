class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cycle = set()
        adj_list = { i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        
        def dfs(course):
            if not adj_list[course]:
                return True
            if course in cycle:
                return False

            cycle.add(course)
            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False

            cycle.remove(course)
            adj_list[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True