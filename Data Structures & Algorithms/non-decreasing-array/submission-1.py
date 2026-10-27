class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        has_changed = False
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                if has_changed:
                    return False
                has_changed = True

                # nums[i - 1] and nums [i - 2] are non-decreasing
                if i > 1 and nums[i] < nums[i - 2]:
                    nums[i] = nums[i - 1]
                else:
                    nums[i - 1] = nums[i]
        return True