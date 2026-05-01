class Solution:
    def trap(self, height: List[int]) -> int:
        # init vars l, r, max_L = 0, max_R = 0, total
        l, r = 0, len(height) - 1
        max_L, max_R, total = height[l], height[r], 0
        
        # formula: min(max_L, max_R) - h[i]
        while l < r:
            if max_L <= max_R:
                curr_water = min(max_L, max_R) - height[l]
                l += 1
                max_L = max(max_L, height[l])
            else:
                curr_water = min(max_L, max_R) - height[r]
                r -= 1
                max_R = max(max_R, height[r])

            if curr_water > 0:
                total += curr_water
        return total