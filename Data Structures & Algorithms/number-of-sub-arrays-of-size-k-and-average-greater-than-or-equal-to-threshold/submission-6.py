class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target_sum = k * threshold
        window_sum = out = l = 0

        for r, num in enumerate(arr):
            window_sum += num
            if r - l + 1 == k:
                if window_sum >= target_sum:
                    out += 1
                window_sum -= arr[l]
                l += 1
        return out