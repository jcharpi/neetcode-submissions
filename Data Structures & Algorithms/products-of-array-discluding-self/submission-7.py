class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix, postfix = [], []

        for i in range(len(nums)):
            if len(prefix) == 0:
                prefix.append(1)
            else:
                prefix.append(prefix[i-1]*nums[i-1])
        
        flipped_nums = nums[::-1]
        for i in range(len(flipped_nums)):
            if len(postfix) == 0:
                postfix.append(1)
            else:
                postfix.append(postfix[i-1]*flipped_nums[i-1])
        
        flipped_postfix = postfix[::-1]
        
        out = []
        for i in range(len(nums)):
            out.append(flipped_postfix[i] * prefix[i])
        return out
