
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        cycle = set()
        course_to_reqs = { i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            course_to_reqs[course].append(prereq)
        
        def dfs(course):
            if not course_to_reqs[course]:
                return True
            if course in cycle:
                return False

            cycle.add(course)

            for prereq in course_to_reqs[course]:
                if not dfs(prereq):
                    return False

            cycle.remove(course)
            course_to_reqs[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True