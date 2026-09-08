public class Solution {
    public bool CanFinish(int numCourses, int[][] prerequisites) {
        var visited = new HashSet<int>();
        var courseToReqs = new Dictionary<int, List<int>>();
        for (int i = 0; i < numCourses; i++) {
            courseToReqs[i] = new List<int>();
        }

        foreach (int[] pair in prerequisites) {
            courseToReqs[pair[0]].Add(pair[1]);
        }

        bool Dfs(int course) {
            if (courseToReqs[course].Count == 0) return true;
            if (visited.Contains(course)) return false;

            visited.Add(course);
            foreach (int preReq in courseToReqs[course]) {
                if (!Dfs(preReq)) return false;
            }

            visited.Remove(course);
            courseToReqs[course] = new List<int>();
            return true;
        }

        for (int course = 0; course < numCourses; course++) {
            if (!Dfs(course)) return false;
        }

        return true;
    }
}
