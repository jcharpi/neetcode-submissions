class Solution {
public:
    int leastInterval(vector<char>& tasks, int n) {
        array<int, 26> task_counts{};
        for (char task : tasks) task_counts[task - 'A']++;

        priority_queue<int> max_heap;
        for (int count : task_counts) if (count) max_heap.push(count);

        queue<pair<int, int>> q;
        int time = 0;

        while (!max_heap.empty() || !q.empty()) {
            time++;

            if (!max_heap.empty()) {
                int count = max_heap.top();
                max_heap.pop();
                if (count - 1 > 0) q.push({count - 1, time + n});
            }

            if (!q.empty() && q.front().second == time) {
                max_heap.push(q.front().first);
                q.pop();
            }
        }

        return time;
    }
};
