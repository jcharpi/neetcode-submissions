class Solution:
    def merge(self, left, right):
        i = j = 0
        out = []
        while left and right and i < len(left) and j < len(right):
            if left[i] < right[j]:
                out.append(left[i])
                i += 1
            else:
                out.append(right[j])
                j += 1
        
        while left and i < len(left):
            out.append(left[i])
            i += 1
        
        while right and j < len(right):
            out.append(right[j])
            j += 1
        
        return out

    def sortArray(self, nums: List[int]) -> List[int]:
        if len(nums) == 1:
            return nums
        
        mid = len(nums) // 2
        sorted_left = self.sortArray(nums[:mid])
        sorted_right = self.sortArray(nums[mid:])

        return self.merge(sorted_left, sorted_right)
