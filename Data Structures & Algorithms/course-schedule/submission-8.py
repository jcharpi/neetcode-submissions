class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_to_prereqs = { course: [] for course in range(numCourses) }
        for course, prereq in prerequisites:
            course_to_prereqs[course].append(prereq)

        visited, cycle = set(), set()

        def dfs(course):
            if course in visited:
                return True
            if course in cycle:
                return False

            cycle.add(course)
            for prereq in course_to_prereqs[course]:
                if not dfs(prereq):
                    return False
            
            cycle.remove(course)
            visited.add(course)
            return True

        for course in range(numCourses):
            if not dfs(course):
                return False
        return True