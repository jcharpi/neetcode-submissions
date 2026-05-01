class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()


        out = []
        for i in range(len(nums)):
            # remove dup issue for loop
            if i != 0 and nums[i-1] == nums[i]:
                continue
            
            # regular two sum
            l, r = i + 1, len(nums) - 1
            while l < r:
                curr_sum = nums[l] + nums[r] + nums[i]
                if curr_sum < 0:
                    l += 1
                elif curr_sum > 0:
                    r -= 1
                else:
                    out.append([nums[l], nums[r], nums[i]])
                    l += 1
                    while l < r and nums[l-1] == nums[l]:
                        l += 1
        return out
