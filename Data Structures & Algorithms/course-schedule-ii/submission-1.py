class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj_list = { i : [] for i in range(numCourses) }
        for course, prereq in prerequisites:
            adj_list[course].append(prereq)
        
        visited, cycle = set(), set()
        out = []
        def dfs(course):
            if course in visited:
                return True
            if course in cycle:
                return False
            
            cycle.add(course)
            for prereq in adj_list[course]:
                if not dfs(prereq):
                    return False

            cycle.remove(course)
            visited.add(course)
            out.append(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return []
        return out