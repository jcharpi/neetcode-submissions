class Solution:
    def rob(self, nums: List[int]) -> int:


        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        cache = { 0 : nums[0], 1 : max(nums[0], nums[1]) }
        max_money = 0
        for i in range(2, len(nums)):
            rob, skip = cache[i - 2] + nums[i], cache[i - 1]
            max_money = max(rob, skip)
            cache[i] = max_money
            print(f"Index {i}:", rob, skip, cache)
        return max_money

# Two decisions: rob a house or skip a house
# because this is every other, we always + 2