class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        read = write = 0

        while write < len(nums) and read < len(nums):
            # write isn't at value: advance read
            if nums[write] != val:
                nums[read] = nums[write]
                read += 1
            write += 1
        return read
