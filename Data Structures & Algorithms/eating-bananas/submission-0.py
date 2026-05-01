class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # what bounds us?
        # only 1 pile per hour
        # - largest height (k will NEVER be greater than largest height)
        # number of hours

        # brute force?
        # check every k <= largest height until the lowest one works
        # i.e. try everything from [1... largest height] <= binary search on this

        # Sort? sort seems good
        # 1, 2, 3, 4
        # h = 9

        l, r = 1, max(piles)
        out = r

        while l <= r:
            k = (l + r) // 2
            
            total_time = 0
            for pile in piles:
                total_time += math.ceil(float(pile) / k)
            if total_time <= h:
                out = k
                r = k - 1
            else:
                l = k + 1
        return out

 
