class Solution {
public:
    int maxProduct(vector<int>& nums) {
        if (ssize(nums) == 1) return nums[0];

        unordered_map<int, pair<int, int>> cache;
        cache[0] = pair{ nums[0], nums[0] };

        int max_product = nums[0];
        function<pair<int, int>(int i)> product_at = [&](int i) -> pair<int, int> {
            if (cache.contains(i)) return cache[i];

            pair<int, int> last_product = product_at(i - 1);
            int curr_min = min({nums[i], 
                last_product.first * nums[i], 
                last_product.second * nums[i]});
            int curr_max = max({nums[i], 
                last_product.first * nums[i], 
                last_product.second * nums[i]});
            max_product = max(max_product, curr_max);
            return cache[i] = pair{ curr_min, curr_max };
        };
        
        product_at(ssize(nums) - 1).second;
        return max_product;
    }
};
