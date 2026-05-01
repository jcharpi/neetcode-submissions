class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # 0, 1

        # Prefix:
        # 1, 1, 2, 8
        # Suffix:
        # 48, 24, 6, 1
        prefix, suffix, i = [], [], 0
        prefix_count, suffix_count = 1, 1

        while i < len(nums):
            if(len(prefix) == 0):
                prefix.append(prefix_count)
            else:
                prefix_count = prefix_count*nums[i-1]
                prefix.append(prefix_count)
            i += 1

        i -= 1

        while i > -1:
            if(len(suffix) == 0):
                suffix.append(suffix_count)
            else:
                suffix_count = suffix_count*nums[i+1]
                suffix.append(suffix_count)
            i -= 1

        out = []
        for j in range(len(nums)):
            flipSuffix = suffix[::-1]
            out.append(prefix[j] * flipSuffix[j])
        return out
        print(prefix)
        print(suffix)