# nums[i] indicates your maximum jump length at that position.

# Return true if you can reach the last index starting from index 0, or false otherwise.

# max distance

# initial thought is that jumping max distance is not always best
# I would think we want to maximize the value we land on, not what value we have

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_index = 0

        for i, num in enumerate(nums):
            if i > max_index:
                break
            max_index = max(max_index, i + num)
            print(i, num, max_index)
        return max_index >= len(nums) - 1