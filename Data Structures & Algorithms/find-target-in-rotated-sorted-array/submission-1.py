class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        # one side sorted, one side not
        while l <= r:
            m = (l + r) // 2
            
            if nums[m] == target:
                return m

            # left side is sorted
            if nums[l] <= nums[m]:
                # target is in the left, sorted side
                if nums[l] <= target < nums[m]:
                    r = m - 1
                
                # target is in right, unsorted side
                else:
                    l = m + 1
            
            # right side is sorted
            else:
                # target is in right, sorted side
                if nums[m] < target <= nums[r]:
                    l = m + 1

                # target is in left, unsorted side
                else:
                    r = m - 1
        return -1