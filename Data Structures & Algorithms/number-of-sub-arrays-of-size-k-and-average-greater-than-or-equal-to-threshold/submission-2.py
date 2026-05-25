class Solution:
    def numOfSubarrays(self, arr: List[int], k: int, threshold: int) -> int:
        target_sum = k * threshold
        window_sum = sum(arr[:k])
        out = 0

        for l in range(len(arr) - k):
            if window_sum >= target_sum:
                out += 1

            window_sum -= arr[l]
            window_sum += arr[l+k]
        
        if window_sum >= target_sum:
            out += 1

        return out