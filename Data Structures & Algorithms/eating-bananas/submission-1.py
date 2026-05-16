class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def isCorrect(n):
            hours = 0
            for pile in piles:
                hours += math.ceil(pile/n)
            return True if hours <= h else False
        
        low, high = 1, max(piles)
        min_hours = float('inf')
        while low <= high:
            mid = (low + high) // 2
            if isCorrect(mid):
                min_hours = min(min_hours, mid)
                high = mid - 1
            else:
                low = mid + 1
        return min_hours
        print(isCorrect(3))