class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Phase 1: find a meeting point inside the cycle
        slow = fast = 0
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Phase 2: walk from start and from meeting point at equal speed;
        # they meet at the cycle entrance, which is the duplicate
        slow = 0
        while True:
            slow = nums[slow]
            fast = nums[fast]
            if slow == fast:
                return slow