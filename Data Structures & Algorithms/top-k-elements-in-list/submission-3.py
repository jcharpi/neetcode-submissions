class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        out = {}
        freq = [[] for i in range(len(nums) + 1)]
        
        for num in nums:
            out[num] = 1 + out.get(num, 0)
        for n, c in out.items():
            print(c)
            print(n)
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res
