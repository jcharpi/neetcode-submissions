class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        def is_turbulent(a, b, c):
            return a < b > c or a > b < c
        
        l, max_length = 0, 1

        for r in range(1, len(arr)):
            if r > 0 and arr[r - 1] == arr[r]:
                l = r
            elif r - l + 1 > 2 and not is_turbulent(arr[r - 2], arr[r - 1], arr[r]):
                l = r - 1
            max_length = max(max_length, r - l + 1)
        return max_length