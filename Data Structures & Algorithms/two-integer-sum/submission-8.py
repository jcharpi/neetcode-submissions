class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hm = {}
        for i, num in enumerate(nums):
            if num in hm:
                return [hm[num], i]
            
            hm[target-num] = i
