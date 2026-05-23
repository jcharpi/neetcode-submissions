class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, window = 0, set()
        for r, num in enumerate(nums):
            if abs(l - r) > k:
                window.remove(nums[l])
                l += 1

            if num in window:
                return True
            
            window.add(num)
        return False

