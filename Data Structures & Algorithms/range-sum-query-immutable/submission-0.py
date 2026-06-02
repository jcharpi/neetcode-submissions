class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = []
        
        prefix = 0
        for num in nums:
            prefix += num
            self.nums.append(prefix)

    def sumRange(self, left: int, right: int) -> int:
        print(self.nums)
        print(self.nums[right])
        return self.nums[right] - self.nums[left - 1] if left else self.nums[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
