class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for _ in range(len(nums) + 1)]
        counts = Counter(nums)

        for num, count in counts.items():
            freq[count].append(num)

        out = []
        for bucket in reversed(freq):
            for num in bucket:
                out.append(num)
                if len(out) == k:
                    return out
                