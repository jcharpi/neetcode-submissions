class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = fast = 0
        first_intersect = 0
        while True:
            fast = nums[nums[fast]]
            slow = nums[slow]
            if fast == slow:
                first_intersect = slow
                break
        
        second_intersect = 0
        while True:
            first_intersect = nums[first_intersect]
            second_intersect = nums[second_intersect]
            if first_intersect == second_intersect:
                return first_intersect