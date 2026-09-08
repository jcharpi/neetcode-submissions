class Solution {
public:
    bool canFinish(int numCourses, vector<vector<int>>& prerequisites) {
        unordered_set<int> visited;
        unordered_map<int, vector<int>> course_to_reqs;
        
        for (vector<int> p : prerequisites) course_to_reqs[p[0]].push_back(p[1]);

        function<bool(int course)> dfs = [&](int course) -> bool {
            if (course_to_reqs[course].empty()) return true;
            if (visited.contains(course)) return false;

            visited.insert(course);

            for (int pre_req : course_to_reqs[course]) {
                if (!dfs(pre_req)) return false;
            }

            visited.erase(course);
            course_to_reqs[course].clear();
            return true;
        };

        for (int course = 0; course < numCourses; course++) {
            if (!dfs(course)) return false;
        }
        return true;
    }
};
