class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_l, max_r = height[l], height[r]
        max_water = 0

        while l < r:
            curr_water = 0
            if max_l > max_r:
                curr_water = min(max_l, max_r) - height[r]
                r -= 1
                max_r = max(max_r, height[r])
            else:
                curr_water = min(max_l, max_r) - height[l]
                l += 1
                max_l = max(max_l, height[l])
            
            if curr_water > 0:
                max_water += curr_water
                
        return max_water