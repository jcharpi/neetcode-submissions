class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        out = []
        curr = []
        nums.sort()

        def dfs():
            if not nums:
                out.append(curr.copy())
                return
            
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue

                num = nums.pop(i)
                curr.append(num)
                dfs()

                nums.insert(i, num)
                curr.pop()

            
        dfs()
        return out
