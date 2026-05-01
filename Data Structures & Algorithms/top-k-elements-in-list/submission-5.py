class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hm = {}
        freq = [[] for i in range(len(nums) + 1)]
        for num in nums:
            hm[num] = 1 + hm.get(num, 0)

        for n, c in hm.items():
            freq[c].append(n)
        
        out = []
        for i in range(len(freq) - 1, 0, -1):
            for j in range(len(freq[i])):
                out.append(freq[i][j])
                if len(out) == k:
                    return out
        print(out)