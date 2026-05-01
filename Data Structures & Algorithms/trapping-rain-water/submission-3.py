class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        maxL, maxR, out = height[l], height[r], 0
        while l < r:
            # key: min(maxL, maxR) - height[i]
            if maxL <= maxR:
                curr_water = min(maxL, maxR) - height[l]
                l += 1
                maxL = max(height[l], maxL)
            else:
                curr_water = min(maxL, maxR) - height[r]
                r -= 1
                maxR = max(height[r], maxR)

            if curr_water > 0:
                out += curr_water
       
        return out