class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        out = len(students)
        student_prefs = Counter(students)

        for sandwich in sandwiches:
            if student_prefs[sandwich] > 0:
                out -= 1
                student_prefs[sandwich] -= 1
            else:
                return out
        return out