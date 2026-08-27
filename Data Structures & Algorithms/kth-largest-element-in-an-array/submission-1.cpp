class Solution {
public:
    int findKthLargest(vector<int>& nums, int k) {
        priority_queue<int, vector<int>, greater<>> min_heap(nums.begin(), nums.end());
        while (ssize(min_heap) > k) min_heap.pop();
        return min_heap.top();
    }
};
