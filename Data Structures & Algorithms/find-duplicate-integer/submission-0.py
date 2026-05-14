class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        hm = {}
        for i, num in enumerate(nums):
            if num in hm:
                hm[num].append(i)
            else:
                hm[num] = [i]
            
        for key, value in hm.items():
            if len(value) > 1:
                return key