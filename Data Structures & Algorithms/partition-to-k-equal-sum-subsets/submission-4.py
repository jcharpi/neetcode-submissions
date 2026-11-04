class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        total = sum(nums)
        if total % k != 0:
            return False
        
        subset_sum = total // k
        buckets = [0] * k

        nums.sort()
        if nums[-1] > subset_sum:
            return False

        def dfs(i):
            if i < 0:
                return True

            for j in range(k):
                if buckets[j] + nums[i] <= subset_sum:
                    buckets[j] += nums[i]
                    if dfs(i - 1):
                        return True
                    buckets[j] -= nums[i]
                if buckets[j] == 0:
                    break
            return False
        
        return dfs(len(nums) - 1)
