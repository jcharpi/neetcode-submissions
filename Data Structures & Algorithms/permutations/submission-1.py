class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        out = []
        curr = []

        def dfs():
            if not nums:
                out.append(curr.copy())
                return
            
            for i in range(len(nums)):
                num = nums.pop(i)
                curr.append(num)
                dfs()

                curr.pop()
                nums.insert(i, num)
        dfs()
        return out