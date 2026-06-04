class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        out = prefix_sum = 0
        hm = { 0 : 1 } # prefix_sum : count

        for i, num in enumerate(nums):
            prefix_sum += num
            target = prefix_sum - k
            if target in hm:
                out += hm[target]
            hm[prefix_sum] = hm.get(prefix_sum, 0) + 1
        return out