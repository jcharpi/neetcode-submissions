class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []
        print(nums)

        for i, num in enumerate(nums):
            if i != 0 and nums[i] == nums[i - 1]:
                continue

            l, r = i + 1, len(nums) - 1
            while l < r:
                nums_sum = num + nums[l] + nums[r]

                if nums_sum < 0:
                    l += 1
                elif nums_sum > 0:
                    r -= 1
                else:
                    out.append([num, nums[l], nums[r]])
                    while l < r and nums[l+1] == nums[l]:
                        l += 1
                    l += 1
        return out