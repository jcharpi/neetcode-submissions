class Solution {
public:
    vector<int> findClosestElements(vector<int>& arr, int k, int x) {
        auto isCloser = [&](int a, int b) -> bool {
            return (abs(a - x) < abs(b - x)) || (abs(a - x) == abs(b - x) && a < b);
        };

        deque<int> window;
        int left = 0;
        for (int right = 0; right < ssize(arr); right++) {
            if (ssize(window) < k) window.push_back(arr[right]);
            else if (isCloser(arr[right], arr[left])) {
                window.push_back(arr[right]);
                window.pop_front();
                left++;
            }
        }
        return vector<int>(window.begin(), window.end());
    }
};