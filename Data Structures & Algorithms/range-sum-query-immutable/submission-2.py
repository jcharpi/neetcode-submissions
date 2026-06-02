class NumArray:

    def __init__(self, nums: List[int]):
        self.prefixes = []
        
        prefix = 0
        for num in nums:
            prefix += num
            self.prefixes.append(prefix)

    def sumRange(self, left: int, right: int) -> int:
        return self.prefixes[right] - self.prefixes[left - 1] if left else self.prefixes[right]


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
