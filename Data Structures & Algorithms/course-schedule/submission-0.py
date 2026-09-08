# You are given an array prerequisites where prerequisites[i] = [a, b] indicates that you must take course b first if you want to take course a.

# The pair [0, 1], indicates that must take course 1 before taking course 0.

# There are a total of numCourses courses you are required to take, labeled from 0 to numCourses - 1.

# Return true if it is possible to finish all courses, otherwise return false.

# look for cycles


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
