
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visited = set()
        course_to_reqs = { i : [] for i in range(numCourses)}
        for course, pre_req in prerequisites:
            course_to_reqs[course].append(pre_req)
        
        def dfs(course):
            if len(course_to_reqs[course]) == 0:
                return True
            if course in visited:
                return False

            visited.add(course)

            for pre_req in course_to_reqs[course]:
                if not dfs(pre_req):
                    return False

            visited.remove(course)
            course_to_reqs[course] = []
            return True
        
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
