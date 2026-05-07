class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = [[] for i in range(len(nums) + 1)]
        counts = {}

        for num in nums:
            counts[num] = counts.get(num, 0) + 1

        for num, count in counts.items():
            freq[count].append(num)

        out = []
        for array_i in range(len(freq) - 1, 0, -1):
            for num in freq[array_i]:
                out.append(num)
                if len(out) == k:
                    return out
                