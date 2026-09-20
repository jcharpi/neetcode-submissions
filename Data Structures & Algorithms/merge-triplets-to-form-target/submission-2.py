# Given
# - 2D array of integers triplets
# - triplets[i] = [ai, bi, ci]

# - target = [x, y, z] which is the triplet we want to obtain

# Operations
# - Choose two different triplets triplets[i] and triplets[j]
# -- Update triplets[j]: [max(ai, aj), max(bi, bj), max(ci, cj)].

# DP intuition: dp[i] represents *WHAT*
# - What do we know?
# -- If, while iterating, we can make the triplet at some point, we can just return True
# -- If some value ai, bi, ci is greater than the target respective value, then that whole triplet cannot be used with the update operation
# --- I would be inclined to think dp[i] represents the most updated triplet we can have that does not violate this point, then by the end we return dp[-1] == target


class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        dp = [0, 0, 0]

        for a, b, c in triplets:
            if (a <= target[0] and 
                b <= target[1] and 
                c <= target[2]):
                dp = [max(dp[0], a), max(dp[1], b), max(dp[2], c)]
                if dp == target:
                    return True
            
        return dp[-1] == target
