class KthLargest {
public:
    priority_queue<int, vector<int>, greater<>> min_heap;
    int k;

    KthLargest(int k, vector<int>& nums) : min_heap(nums.begin(), nums.end()), k(k) {
        while (ssize(min_heap) > k) min_heap.pop();
    }
    
    int add(int val) {
        min_heap.push(val);
        if (ssize(min_heap) > k) min_heap.pop();
        return min_heap.top();
    }
};
