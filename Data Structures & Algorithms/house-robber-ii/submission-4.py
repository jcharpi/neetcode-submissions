class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        def rob_range(start, end):
            two_houses_back = one_house_back = 0
            for i in range(start, end):
                curr = max(two_houses_back + nums[i], one_house_back)
                two_houses_back, one_house_back = one_house_back, curr
            return max(two_houses_back, one_house_back)

        skip_first = rob_range(1, len(nums))
        skip_last = rob_range(0, len(nums) - 1)
        return max(skip_first, skip_last)