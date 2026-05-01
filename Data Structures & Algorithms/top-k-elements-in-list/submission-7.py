class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        for n, f in count.items():
            freq[f].append(n)
        
        out = []
        for a in range(len(freq) - 1, 0, -1):
            for n in freq[a]:
                out.append(n)
                if len(out) == k:
                    return out