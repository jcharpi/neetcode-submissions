class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        read, write = 0, 1

        while write < len(nums):
        # while the two are equal, increment write
            while write < len(nums) and nums[write] == nums[read]:
                print(nums[write])
                write += 1
            if write < len(nums):
                read += 1
                nums[read] = nums[write]
            print(nums)
            write += 1
        return len(nums[:read + 1])