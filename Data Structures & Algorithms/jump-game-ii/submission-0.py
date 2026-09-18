class Solution:
    def jump(self, nums: List[int]) -> int:
        i = out = 0
        while i < len(nums) - 1:
            if i + nums[i] >= len(nums) - 1:
                return out + 1
            
            max_reachable = 0
            for j in range(i, i + nums[i] + 1):
                if j + nums[j] > max_reachable:
                    max_reachable = j + nums[j]
                    max_j = j
            i = max_j
            out += 1
        return out

        # nums[i] represents the maximum length of a jump towards the right from index i
        # - same as jump game i
        
        # always a valid answer

        # dp where optimum is as far as we can get ending at i
        # can we do greedy?

        # is max jump area reachable valid

        # what jumps do we want to take?
        # 1 jump to 1st index, 1 jump to end
        # what is special about index 1? it has a large number at it
        # what does that mean? it can take us further, meaning less hops
        # so we want to maximize nums[i] that is reachable... but how do we do that technically?

        # if we have index 0: 2, we can reach 2, so we need to compare index 1 and index 2 to see which gets further

