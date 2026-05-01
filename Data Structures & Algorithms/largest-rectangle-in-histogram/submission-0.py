class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        # iterate through, checking left and right for max
        # max = max(curr, max)
        
        # skip 

        max_area = 0
        stack = []

        for i in range(len(heights)):
            start = i
            while stack and stack[-1][1] > heights[i]:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, heights[i]))

        for i, h in stack:
            max_area = max(max_area, h * (len(heights) - i))

        return max_area