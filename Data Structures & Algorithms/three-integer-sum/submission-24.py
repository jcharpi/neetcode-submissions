class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        out = []

        for i in range(len(nums)):
            if i != 0 and nums[i] == nums[i-1]:
                continue

            l, r = i+1, len(nums) - 1
            while l < r:
                if nums[l] + nums[r] + nums[i] > 0:
                    r -= 1
                elif nums[l] + nums[r] + nums[i] < 0:
                    l += 1
                else:
                    out.append([nums[l], nums[r], nums[i]])
                    l += 1
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
        return out

