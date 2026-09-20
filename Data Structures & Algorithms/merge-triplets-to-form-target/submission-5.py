class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        out = [0, 0, 0]
        for a, b, c in triplets:
            if (a <= target[0] and 
                b <= target[1] and 
                c <= target[2]):
                out = [max(out[0], a), max(out[1], b), max(out[2], c)]
                if out == target:
                    return True

        return False
