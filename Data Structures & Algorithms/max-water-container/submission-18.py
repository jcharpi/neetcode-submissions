class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l, r = 0, len(heights) - 1

        most_water = 0
        while l < r:
            length = r - l
            height = min(heights[l], heights[r])
            curr_water = length*height
            if heights[l] < heights[r]:
                l += 1
            else:
                r -= 1
            
            most_water = max(most_water, curr_water)
        return most_water
