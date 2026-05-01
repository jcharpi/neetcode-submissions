class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # initialize pointers
        l, r = 0, len(heights) - 1

        max_area = 0

        while l < r:
            # initalize max area
            height = min(heights[l], heights[r])
            width = r - l
            curr_area = height * width

            # move shorter pointer
            if heights[r] >= heights[l]:
                l += 1
            else:
                r -= 1
            
            max_area = max(max_area, curr_area)
        return max_area
