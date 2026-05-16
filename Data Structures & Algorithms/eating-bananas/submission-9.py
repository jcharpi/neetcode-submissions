class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isCorrect(bananas_per_hour):
            return sum(math.ceil(pile / bananas_per_hour) for pile in piles) <= h

        low, high = 1, max(piles)
        while low <= high:
            mid = (low + high) // 2
            if isCorrect(mid):
                high = mid - 1
            else:
                low = mid + 1
        return low