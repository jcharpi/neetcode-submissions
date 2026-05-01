class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        max_L = height[l]
        max_R = height[r]
        out = 0
        # min(maxL,maxR) - height[i]
        while l < r:
            curr = 0
            if max_L < max_R:
                curr = min(max_L, max_R) - height[l]
                l += 1
                max_L = max(height[l], max_L)
            else:
                curr = min(max_L, max_R) - height[r]
                r -= 1
                max_R = max(height[r], max_R)
            
            if curr > 0:
                out += curr

        return out