class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        for read in range(len(nums)):
            if read < 1 or nums[read] != nums[write - 1]:
                nums[write] = nums[read]
                write += 1
        return write