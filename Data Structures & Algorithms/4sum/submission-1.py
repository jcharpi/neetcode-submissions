class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums.sort()
        out = []

        for a in range(len(nums)):
            if a != 0 and nums[a] == nums[a - 1]:
                continue
            for b in range(a + 1, len(nums)):
                c, d = b + 1, len(nums) - 1

                if b != a + 1 and nums[b] == nums[b - 1]:
                    continue
                
                while c < d:
                    nums_sum = nums[a] + nums[b] + nums[c] + nums[d]
                    
                    if nums_sum < target:
                        c += 1
                    elif nums_sum > target:
                        d -= 1
                    else:
                        out.append([nums[a], nums[b], nums[c], nums[d]])
                        while c < d and nums[c] == nums[c + 1]:
                            c += 1
                        while c < d and nums[d] == nums[d - 1]:
                            d -= 1
                        c += 1
                        d -= 1
        return out