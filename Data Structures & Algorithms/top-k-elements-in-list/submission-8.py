class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for count, number in count.items():
            freq[number].append(count)

        out = []
        for arr in range(len(freq) - 1, 0, -1):
            for value in freq[arr]:
                out.append(value)
                if len(out) == k:
                    return out
        