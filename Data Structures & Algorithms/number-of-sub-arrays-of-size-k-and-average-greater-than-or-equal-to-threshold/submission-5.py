class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target_sum = k * threshold
        window_sum = sum(arr[:k])
        out = 1 if window_sum >= target_sum else 0

        for r in range(k, len(arr)):
            window_sum += arr[r] - arr[r - k]
            if window_sum >= target_sum:
                out += 1
        return out