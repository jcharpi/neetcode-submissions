class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1

        def isPeak(i):
            if ((i > 0 and nums[i - 1] > nums[i]) or 
                (i < len(nums) - 1 and nums[i + 1] > nums[i])):
                return False
            return True        
            
        while l < r:
            m = (l + r) // 2
            if isPeak(m):
                return m

            if nums[m] < nums[m + 1]:
                l = m + 1
            else:
                r = m - 1
        return l