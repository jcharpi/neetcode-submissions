class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = defaultdict(list)
        counts = defaultdict(int)

        for num in nums:
            counts[num] += 1

        for num, count in counts.items():
            freq[count].append(num)

        out = []
        for i in range(len(nums), 0, -1):
            for num in freq[i]:
                out.append(num)
                if len(out) == k:
                    return out
                